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
        # Set the main_currency based on the selected account
        expense.main_currency = expense.account.currency
        if commit:
            expense.save()
        return expense


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(required=True, validators=[MinValueValidator(0.00)])

    class Meta:
        model = Income
        fields = ["category", "account", "amount", "date", "description"]
