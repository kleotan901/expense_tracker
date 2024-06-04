from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    pass


class Account(models.Model):
    account_type = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.account_type}: {self.balance}"
