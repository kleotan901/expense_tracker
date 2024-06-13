from django.db import models
from django.db.models import F

from account.models import Account


class Category(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=7, choices=CATEGORY_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"


class Expense(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"category_type": "expense"},
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    converted_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True
    )
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category}"

    def save(self, *args, **kwargs):
        if self.amount is None:
            self.amount = 0.00
        super().save(*args, **kwargs)


class Income(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"category_type": "income"},
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    converted_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True
    )
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.category}"

    def save(self, *args, **kwargs):
        if self.amount is None:
            self.amount = 0.00
        super().save(*args, **kwargs)
