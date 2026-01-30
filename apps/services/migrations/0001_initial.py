from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customers", "0001_initial"),
        ("vehicles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Nome")),
                ("document", models.CharField(blank=True, max_length=20, verbose_name="CPF")),
                ("role", models.CharField(blank=True, max_length=100, verbose_name="Função")),
                ("active", models.BooleanField(default=True, verbose_name="Ativo")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Criado em")),
            ],
            options={
                "verbose_name": "Funcionário",
                "verbose_name_plural": "Funcionários",
            },
        ),
        migrations.CreateModel(
            name="ServiceOrder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("service_date", models.DateField(default=django.utils.timezone.localdate, verbose_name="Data")),
                ("plate", models.CharField(max_length=10, verbose_name="Placa")),
                ("vehicle_description", models.CharField(max_length=150, verbose_name="Veículo")),
                ("description", models.TextField(blank=True, verbose_name="Descrição do serviço")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("open", "Aberta"),
                            ("in_progress", "Em andamento"),
                            ("waiting_parts", "Aguardando peças"),
                            ("done", "Concluída"),
                            ("cancelled", "Cancelada"),
                        ],
                        default="open",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "labor_cost",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Mão de obra"),
                ),
                ("total_value", models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Valor")),
                ("nf_number", models.CharField(blank=True, max_length=50, verbose_name="NF")),
                ("ss_number", models.CharField(blank=True, max_length=50, verbose_name="SS")),
                ("opened_at", models.DateTimeField(auto_now_add=True, verbose_name="Aberta em")),
                ("closed_at", models.DateTimeField(blank=True, null=True, verbose_name="Fechada em")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_orders",
                        to="customers.customer",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="service_orders",
                        to="services.employee",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="service_orders",
                        to="vehicles.vehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ordem de Serviço",
                "verbose_name_plural": "Ordens de Serviço",
            },
        ),
    ]
