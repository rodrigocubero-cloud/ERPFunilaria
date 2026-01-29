from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("issue_date", models.DateField(verbose_name="Data de emissão")),
                ("due_date", models.DateField(verbose_name="Data de vencimento")),
                ("total", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Total")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pendente"),
                            ("paid", "Pago"),
                            ("overdue", "Vencido"),
                            ("cancelled", "Cancelado"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                ("notes", models.TextField(blank=True, verbose_name="Observações")),
                (
                    "service_order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice",
                        to="services.serviceorder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fatura",
                "verbose_name_plural": "Faturas",
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("paid_at", models.DateTimeField(verbose_name="Pago em")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Valor")),
                (
                    "method",
                    models.CharField(
                        choices=[
                            ("cash", "Dinheiro"),
                            ("card", "Cartão"),
                            ("transfer", "Transferência"),
                            ("pix", "PIX"),
                        ],
                        max_length=20,
                        verbose_name="Método",
                    ),
                ),
                ("notes", models.TextField(blank=True, verbose_name="Observações")),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="billing.invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pagamento",
                "verbose_name_plural": "Pagamentos",
            },
        ),
    ]
