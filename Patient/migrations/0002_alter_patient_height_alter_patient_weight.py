# Generated by Django 5.0.2 on 2024-03-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Patient", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="height",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="patient",
            name="weight",
            field=models.IntegerField(null=True),
        ),
    ]