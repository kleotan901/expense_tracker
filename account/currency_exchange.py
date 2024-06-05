from decimal import Decimal

import requests
from django.db.models import QuerySet

from account.models import Currency
from expense_tracker.settings import CURRENCY_EXCHANGE_API_KEY


def get_exchange_rate(base_currency, transaction_currency):
    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_EXCHANGE_API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and 'conversion_rates' in data:
        return data['conversion_rates'].get(transaction_currency)
    return None


def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate:
        converted_amount = amount * Decimal(exchange_rate)
        return converted_amount


def get_total_amount(operation_type: QuerySet) -> float:
    base_currency = Currency.objects.get(id=1)
    result = 0

    for operation in operation_type:
        if operation.account.currency == base_currency.main_currency:
            result += operation.amount
        else:
            converted_amount = convert_currency(
                operation.amount,
                operation.account.currency,
                base_currency.main_currency
            )
            result += converted_amount
    return result


def get_accounts_balance(accounts: QuerySet) -> float:
    base_currency = Currency.objects.get(id=1)
    result = 0

    for account in accounts:
        if account.currency == base_currency.main_currency:
            result += account.balance
        else:
            converted_amount = convert_currency(
                account.balance,
                account.currency,
                base_currency.main_currency
            )
            result += converted_amount
    return result
