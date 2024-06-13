from django.contrib.auth.models import AbstractUser
from django.db import models

from account.currency_list import CURRENCY_CHOICES


class UserAccount(AbstractUser):
    pass


class Currency(models.Model):
    main_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.main_currency


class Account(models.Model):
    account_type = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    converted_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return f"{self.account_type}: {self.balance} {self.currency}"
