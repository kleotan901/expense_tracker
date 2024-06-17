from decimal import Decimal

from django import forms
from django.core.validators import MinValueValidator

from account.models import Account
from transaction.models import Category, Expense, Income


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "category_type"]

    def save(self, commit=True):
        category = super().save(commit=False)
        category.owner = category.user
        if commit:
            category.save()
        return category


class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(required=True, validators=[MinValueValidator(0.00)])

    class Meta:
        model = Expense
        fields = ["category", "account", "amount", "date", "description"]

    def __init__(self, *args, **kwargs):
        # Extract the 'user' keyword argument and remove 'user' from kwargs dict
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["account"].queryset = Account.objects.filter(user=user)
            self.fields["category"].queryset = Category.objects.filter(owner=user, category_type="expense")

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

    def __init__(self, *args, **kwargs):
        # Extract the 'user' keyword argument and remove 'user' from kwargs dict
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["account"].queryset = Account.objects.filter(user=user)
            self.fields["category"].queryset = Category.objects.filter(owner=user, category_type="income")

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
