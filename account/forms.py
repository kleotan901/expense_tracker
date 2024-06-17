from decimal import Decimal

from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account, Currency, UserAccount
from account.utility import get_exchange_rate


class UserAccountCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "currency_id")


class UserCurrencyUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['currency_id']


class AccountForm(forms.ModelForm):
    balance = forms.DecimalField(required=True)

    class Meta:
        model = Account
        fields = ["account_type", "balance", "currency"]

    def save(self, commit=True):
        account = super().save(commit=False)
        base_currency = account.user.currency_id.code
        account.conversion_rate = get_exchange_rate(account.currency, base_currency)
        account.converted_balance = Decimal(account.balance) * Decimal(account.conversion_rate)
        if commit:
            account.save()
        return account
