# Generated by Django 5.0.6 on 2024-06-15 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0002_category_creator"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="creator",
            new_name="owner",
        ),
    ]