from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="Nome")),
                ("document", models.CharField(max_length=20, unique=True, verbose_name="CPF/CNPJ")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="E-mail")),
                ("phone", models.CharField(blank=True, max_length=20, verbose_name="Telefone")),
                ("address", models.TextField(blank=True, verbose_name="Endereço")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Criado em")),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
    ]
