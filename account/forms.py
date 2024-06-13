from decimal import Decimal

from django import forms

from account.models import Account, Currency
from account.utility import get_exchange_rate


class AccountForm(forms.ModelForm):
    balance = forms.DecimalField(required=True)

    class Meta:
        model = Account
        fields = ["account_type", "balance", "currency"]

    def save(self, commit=True):
        account = super().save(commit=False)
        base_currency = Currency.objects.get(id=1).main_currency
        account.conversion_rate = get_exchange_rate(account.currency, base_currency)
        account.converted_balance = Decimal(account.balance) * Decimal(account.conversion_rate)
        if commit:
            account.save()
        return account
