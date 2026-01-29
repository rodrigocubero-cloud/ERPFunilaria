from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

import pdfplumber

from apps.customers.models import Customer
from apps.services.models import ServiceOrder
from apps.vehicles.models import Vehicle


CNPJ_RE = re.compile(r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b")
PLATE_RE = re.compile(r"\b[A-Z]{3}-?\d{4}\b|\b[A-Z]{3}\d[A-Z0-9]\d{2}\b")
SINISTRO_RE = re.compile(r"Sinistro\s*([A-Z0-9-./]+)", re.IGNORECASE)
APPROVAL_RE = re.compile(r"Total\s+Aprovado\s*R\$\s*([\d.]+,\d{2})", re.IGNORECASE)
DATE_RE = re.compile(r"\b(\d{2}/\d{2}/\d{4})\b")


@dataclass
class OrcamentoData:
    customer_name: str | None
    customer_document: str | None
    plate: str | None
    vehicle_description: str | None
    total_approved: Decimal
    service_date: datetime.date
    ss_number: str | None


def parse_currency(value: str) -> Decimal:
    normalized = value.replace(".", "").replace(",", ".")
    try:
        return Decimal(normalized)
    except InvalidOperation as exc:
        raise CommandError(f"Valor monetário inválido: {value}") from exc


def extract_text(pdf_path: Path) -> str:
    with pdfplumber.open(str(pdf_path)) as pdf:
        pages = [page.extract_text() or "" for page in pdf.pages]
    return "\n".join(pages)


def extract_customer(lines: list[str]) -> tuple[str | None, str | None]:
    for idx, line in enumerate(lines):
        if CNPJ_RE.search(line):
            document = CNPJ_RE.search(line).group(0)
            name = lines[idx - 1].strip() if idx > 0 else None
            return name or None, document
    return None, None


def extract_plate(text: str) -> str | None:
    match = PLATE_RE.search(text)
    return match.group(0) if match else None


def extract_vehicle_description(lines: list[str], plate: str | None) -> str | None:
    if not plate:
        return None
    for line in lines:
        if plate in line:
            parts = line.split(plate, 1)
            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip()
    return None


def extract_service_date(text: str) -> datetime.date:
    dates = DATE_RE.findall(text)
    if not dates:
        return timezone.localdate()
    for date in dates:
        try:
            return datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError:
            continue
    return timezone.localdate()


def extract_total_approved(text: str) -> Decimal:
    values = [parse_currency(match) for match in APPROVAL_RE.findall(text)]
    if values:
        return sum(values, Decimal("0"))
    return Decimal("0")


def extract_ss_number(text: str) -> str | None:
    match = SINISTRO_RE.search(text)
    return match.group(1) if match else None


def parse_orcamento(pdf_path: Path) -> OrcamentoData:
    text = extract_text(pdf_path)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    customer_name, customer_document = extract_customer(lines)
    plate = extract_plate(text)
    vehicle_description = extract_vehicle_description(lines, plate)
    total_approved = extract_total_approved(text)
    service_date = extract_service_date(text)
    ss_number = extract_ss_number(text)
    return OrcamentoData(
        customer_name=customer_name,
        customer_document=customer_document,
        plate=plate,
        vehicle_description=vehicle_description,
        total_approved=total_approved,
        service_date=service_date,
        ss_number=ss_number,
    )


class Command(BaseCommand):
    help = "Importa PDFs de orçamento aprovados a partir de uma pasta."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            default="Orçamentos",
            help="Pasta com os PDFs aprovados (padrão: Orçamentos na raiz do projeto).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        base_path = Path(options["path"]).expanduser()
        if not base_path.exists():
            raise CommandError(f"Pasta não encontrada: {base_path}")

        pdf_files = sorted(base_path.glob("*.pdf"))
        if not pdf_files:
            self.stdout.write(self.style.WARNING("Nenhum PDF encontrado."))
            return

        for pdf_path in pdf_files:
            data = parse_orcamento(pdf_path)
            if not data.customer_document:
                self.stdout.write(
                    self.style.WARNING(f"CNPJ não encontrado em {pdf_path.name}, ignorando.")
                )
                continue

            customer, _ = Customer.objects.get_or_create(
                document=data.customer_document,
                defaults={"name": data.customer_name or data.customer_document},
            )

            vehicle = None
            if data.plate:
                vehicle, _ = Vehicle.objects.get_or_create(
                    plate=data.plate,
                    defaults={
                        "customer": customer,
                        "brand": "Não informado",
                        "model": data.vehicle_description or "Não informado",
                        "year": timezone.localdate().year,
                    },
                )

            ServiceOrder.objects.create(
                customer=customer,
                vehicle=vehicle,
                plate=data.plate or "N/I",
                vehicle_description=data.vehicle_description or "Não informado",
                total_value=data.total_approved,
                service_date=data.service_date,
                ss_number=data.ss_number or "",
            )

            self.stdout.write(self.style.SUCCESS(f"Importado: {pdf_path.name}"))
