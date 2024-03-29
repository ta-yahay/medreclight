# Generated by Django 5.0.2 on 2024-03-08 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "role",
                    models.CharField(
                        choices=[("doctor", "doctor"), ("patient", "patient")],
                        default="patient",
                        max_length=20,
                    ),
                ),
                ("ssn", models.CharField(blank=True, max_length=50)),
                ("phone", models.CharField(blank=True, max_length=50)),
                ("city", models.CharField(blank=True, max_length=70)),
                ("address", models.CharField(blank=True, max_length=50)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "male"), ("female", "female")],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
