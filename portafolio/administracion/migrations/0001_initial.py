# Generated by Django 4.1.4 on 2022-12-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proyectos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("foto", models.CharField(max_length=1000)),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
            ],
        ),
    ]
