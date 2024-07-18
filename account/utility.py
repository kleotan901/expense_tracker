import requests

from expense_tracker.settings import CURRENCY_EXCHANGE_API_KEY


def get_exchange_rate(base_currency, transaction_currency):
    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_EXCHANGE_API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and "conversion_rates" in data:
        return data["conversion_rates"].get(transaction_currency)
    return None
