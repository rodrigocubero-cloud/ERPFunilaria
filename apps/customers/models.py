from django.db import models


class Customer(models.Model):
    name = models.CharField("Nome", max_length=200)
    document = models.CharField("CPF/CNPJ", max_length=20, unique=True)
    email = models.EmailField("E-mail", blank=True)
    phone = models.CharField("Telefone", max_length=20, blank=True)
    address = models.TextField("Endereço", blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return f"{self.name} ({self.document})"
