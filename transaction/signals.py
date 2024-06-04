from django.db.models import F
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Expense, Income, Account


@receiver(pre_save, sender=Expense)
def update_account_balance_on_expense_save(sender, instance, **kwargs):
    if instance.pk is not None:
        # Updating an existing expense
        previous_instance = Expense.objects.get(pk=instance.pk)
        balance_difference = instance.amount - previous_instance.amount
        instance.account.balance = F("balance") - balance_difference
    else:
        # Creating a new expense
        instance.account.balance = F("balance") - instance.amount
    instance.account.save()


@receiver(pre_delete, sender=Expense)
def update_account_balance_on_expense_delete(sender, instance, **kwargs):
    instance.account_type.balance = F("balance") + instance.amount
    instance.account_type.save()


@receiver(pre_save, sender=Income)
def update_account_balance_on_income_save(sender, instance, **kwargs):
    if instance.pk is not None:
        # Updating an existing income
        previous_instance = Income.objects.get(pk=instance.pk)
        balance_difference = instance.amount - previous_instance.amount
        instance.account.balance = F("balance") + balance_difference
    else:
        # Creating a new income
        instance.account.balance = F("balance") + instance.amount
    instance.account.save()


@receiver(pre_delete, sender=Income)
def update_account_balance_on_income_delete(sender, instance, **kwargs):
    instance.account_type.balance = F("balance") - instance.amount
    instance.account_type.save()
