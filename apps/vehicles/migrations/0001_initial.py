from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("plate", models.CharField(max_length=10, unique=True, verbose_name="Placa")),
                ("brand", models.CharField(max_length=100, verbose_name="Marca")),
                ("model", models.CharField(max_length=100, verbose_name="Modelo")),
                ("year", models.PositiveIntegerField(verbose_name="Ano")),
                ("color", models.CharField(blank=True, max_length=50, verbose_name="Cor")),
                ("vin", models.CharField(blank=True, max_length=50, verbose_name="Chassi")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="customers.customer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Veículo",
                "verbose_name_plural": "Veículos",
            },
        ),
    ]
