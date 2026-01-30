from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Part",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sku", models.CharField(max_length=50, unique=True, verbose_name="SKU")),
                ("name", models.CharField(max_length=200, verbose_name="Nome")),
                ("unit", models.CharField(default="un", max_length=20, verbose_name="Unidade")),
                ("cost", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Custo")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Preço")),
                (
                    "quantity",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Quantidade"),
                ),
            ],
            options={
                "verbose_name": "Peça",
                "verbose_name_plural": "Peças",
            },
        ),
        migrations.CreateModel(
            name="InventoryTransaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "quantity",
                    models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Quantidade"),
                ),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("in", "Entrada"), ("out", "Saída")],
                        max_length=3,
                        verbose_name="Tipo",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Criado em")),
                ("notes", models.TextField(blank=True, verbose_name="Observações")),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="inventory.part",
                    ),
                ),
                (
                    "service_order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="inventory_transactions",
                        to="services.serviceorder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movimentação de estoque",
                "verbose_name_plural": "Movimentações de estoque",
            },
        ),
    ]
