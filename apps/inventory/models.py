from django.db import models

from apps.services.models import ServiceOrder


class Part(models.Model):
    sku = models.CharField("SKU", max_length=50, unique=True)
    name = models.CharField("Nome", max_length=200)
    unit = models.CharField("Unidade", max_length=20, default="un")
    cost = models.DecimalField("Custo", max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0)
    quantity = models.DecimalField("Quantidade", max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Peça"
        verbose_name_plural = "Peças"

    def __str__(self) -> str:
        return f"{self.sku} - {self.name}"


class InventoryTransaction(models.Model):
    TRANSACTION_TYPES = [
        ("in", "Entrada"),
        ("out", "Saída"),
    ]

    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="transactions")
    service_order = models.ForeignKey(
        ServiceOrder,
        on_delete=models.SET_NULL,
        related_name="inventory_transactions",
        blank=True,
        null=True,
    )
    quantity = models.DecimalField("Quantidade", max_digits=10, decimal_places=2)
    transaction_type = models.CharField("Tipo", max_length=3, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    notes = models.TextField("Observações", blank=True)

    class Meta:
        verbose_name = "Movimentação de estoque"
        verbose_name_plural = "Movimentações de estoque"

    def __str__(self) -> str:
        return f"{self.part} ({self.get_transaction_type_display()})"
