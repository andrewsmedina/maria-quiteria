# Generated by Django 3.0.6 on 2020-06-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0019_auto_20200627_1406"),
    ]

    operations = [
        migrations.AlterField(
            model_name="citycouncilexpense",
            name="external_file_code",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Código do arquivo (externo)"
            ),
        ),
        migrations.AlterField(
            model_name="citycouncilexpense",
            name="external_file_line",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Linha do arquivo (externo)"
            ),
        ),
    ]
