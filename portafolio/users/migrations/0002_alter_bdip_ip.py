# Generated by Django 4.1.4 on 2022-12-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bdip", name="ip", field=models.CharField(max_length=200),
        ),
    ]
