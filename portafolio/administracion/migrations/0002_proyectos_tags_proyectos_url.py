# Generated by Django 4.1.4 on 2022-12-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administracion", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="proyectos",
            name="tags",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="proyectos",
            name="url",
            field=models.CharField(default="", max_length=1000),
        ),
    ]