# Generated by Django 3.1.2 on 2020-10-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0022_historical_citycouncil"),
    ]

    operations = [
        migrations.CreateModel(
            name="SyncInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                ("date", models.DateField(verbose_name="Data alvo")),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("camara", "Câmara Municipal"),
                            ("prefeitura", "Prefeitura"),
                        ],
                        db_index=True,
                        max_length=20,
                        verbose_name="Fonte",
                    ),
                ),
                (
                    "succeed",
                    models.BooleanField(
                        null=True, verbose_name="Concluída com sucesso?"
                    ),
                ),
                ("response", models.JSONField(null=True, verbose_name="Resposta")),
            ],
        ),
        migrations.AlterField(
            model_name="citycouncilrevenue",
            name="external_code",
            field=models.PositiveIntegerField(
                db_index=True, unique=True, verbose_name="Código externo"
            ),
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilrevenue",
            name="external_code",
            field=models.PositiveIntegerField(
                db_index=True, verbose_name="Código externo"
            ),
        ),
    ]