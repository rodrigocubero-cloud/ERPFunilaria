from django.db import models
from django.utils import timezone

from apps.customers.models import Customer
from apps.vehicles.models import Vehicle


class Employee(models.Model):
    name = models.CharField("Nome", max_length=150)
    document = models.CharField("CPF", max_length=20, blank=True)
    role = models.CharField("Função", max_length=100, blank=True)
    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self) -> str:
        return self.name


class ServiceOrder(models.Model):
    STATUS_CHOICES = [
        ("open", "Aberta"),
        ("in_progress", "Em andamento"),
        ("waiting_parts", "Aguardando peças"),
        ("done", "Concluída"),
        ("cancelled", "Cancelada"),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="service_orders"
    )
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.SET_NULL, related_name="service_orders", blank=True, null=True
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="service_orders",
        blank=True,
        null=True,
    )
    service_date = models.DateField("Data", default=timezone.localdate)
    plate = models.CharField("Placa", max_length=10)
    vehicle_description = models.CharField("Veículo", max_length=150)
    description = models.TextField("Descrição do serviço", blank=True)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="open")
    labor_cost = models.DecimalField("Mão de obra", max_digits=10, decimal_places=2, default=0)
    total_value = models.DecimalField("Valor", max_digits=10, decimal_places=2, default=0)
    nf_number = models.CharField("NF", max_length=50, blank=True)
    ss_number = models.CharField("SS", max_length=50, blank=True)
    opened_at = models.DateTimeField("Aberta em", auto_now_add=True)
    closed_at = models.DateTimeField("Fechada em", blank=True, null=True)

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"

    def __str__(self) -> str:
        return f"OS #{self.id} - {self.plate} - {self.customer}"
