# Generated by Django 5.0.2 on 2024-03-07 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Readings", "0003_alter_bloodp_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glucose",
            name="date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]