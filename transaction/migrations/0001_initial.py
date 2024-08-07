# Generated by Django 5.0.6 on 2024-06-13 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
                (
                    "category_type",
                    models.CharField(
                        choices=[("income", "Income"), ("expense", "Expense")],
                        max_length=7,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expense",
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
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "converted_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("date", models.DateField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        limit_choices_to={"category_type": "expense"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="transaction.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Income",
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
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "converted_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("date", models.DateField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        limit_choices_to={"category_type": "income"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="transaction.category",
                    ),
                ),
            ],
        ),
    ]
