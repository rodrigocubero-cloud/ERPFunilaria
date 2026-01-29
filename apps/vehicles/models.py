from django.db import models

from apps.customers.models import Customer


class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="vehicles")
    plate = models.CharField("Placa", max_length=10, unique=True)
    brand = models.CharField("Marca", max_length=100)
    model = models.CharField("Modelo", max_length=100)
    year = models.PositiveIntegerField("Ano")
    color = models.CharField("Cor", max_length=50, blank=True)
    vin = models.CharField("Chassi", max_length=50, blank=True)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self) -> str:
        return f"{self.plate} - {self.brand} {self.model}"
