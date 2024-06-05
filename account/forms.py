from django import forms

from account.models import Account, Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["account_type", "balance", "currency"]
