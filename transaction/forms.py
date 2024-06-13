from decimal import Decimal

from django import forms
from django.core.validators import MinValueValidator
from transaction.models import Category, Expense, Income


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(required=True, validators=[MinValueValidator(0.00)])

    class Meta:
        model = Expense
        fields = ["category", "account", "amount", "date", "description"]

    def save(self, commit=True):
        expense = super().save(commit=False)
        expense.converted_amount = Decimal(expense.account.conversion_rate) * Decimal(
            expense.amount
        )
        # change balance of the account
        expense.account.converted_balance -= expense.converted_amount
        if commit:
            expense.save()
        return expense


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(required=True, validators=[MinValueValidator(0.00)])

    class Meta:
        model = Income
        fields = ["category", "account", "amount", "date", "description"]

    def save(self, commit=True):
        income = super().save(commit=False)
        income.converted_amount = Decimal(income.account.conversion_rate) * Decimal(
            income.amount
        )
        # change balance of the account
        income.account.converted_balance += income.converted_amount
        if commit:
            income.save()
        return income
