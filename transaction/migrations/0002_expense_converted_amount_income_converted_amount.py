# Generated by Django 5.0.6 on 2024-06-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="converted_amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10
            ),
        ),
        migrations.AddField(
            model_name="income",
            name="converted_amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10
            ),
        ),
    ]