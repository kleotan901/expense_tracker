from django import forms
from django.core.validators import MinValueValidator

from transaction.models import Category, Expense, Income


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(
        required=True,
        validators=[MinValueValidator(0.00)]
    )

    class Meta:
        model = Expense
        fields = "__all__"


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(
        required=True,
        validators=[MinValueValidator(0.00)]
    )

    class Meta:
        model = Income
        fields = "__all__"
