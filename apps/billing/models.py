from django.db import models

from apps.services.models import ServiceOrder


class Invoice(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("paid", "Pago"),
        ("overdue", "Vencido"),
        ("cancelled", "Cancelado"),
    ]

    service_order = models.OneToOneField(
        ServiceOrder, on_delete=models.CASCADE, related_name="invoice"
    )
    issue_date = models.DateField("Data de emissão")
    due_date = models.DateField("Data de vencimento")
    total = models.DecimalField("Total", max_digits=10, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="pending")
    notes = models.TextField("Observações", blank=True)

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    def __str__(self) -> str:
        return f"Fatura #{self.id} - OS {self.service_order_id}"


class Payment(models.Model):
    METHOD_CHOICES = [
        ("cash", "Dinheiro"),
        ("card", "Cartão"),
        ("transfer", "Transferência"),
        ("pix", "PIX"),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    paid_at = models.DateTimeField("Pago em")
    amount = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    method = models.CharField("Método", max_length=20, choices=METHOD_CHOICES)
    notes = models.TextField("Observações", blank=True)

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self) -> str:
        return f"Pagamento {self.amount} - {self.get_method_display()}"
