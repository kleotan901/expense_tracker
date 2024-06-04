from django import forms

from transaction.models import Category, Expense, Income


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
