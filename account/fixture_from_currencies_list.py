# Create an empty list to store dictionaries
import json

from account.currency_list import CURRENCY_CHOICES

currencies = []
pk = 1
# Loop through CURRENCY_CHOICES and create dictionaries
for code, name in CURRENCY_CHOICES:
    currency = {
        "model": "account.currency",
        "pk": pk,
        "fields": {"code": code, "main_currency": name},
    }
    currencies.append(currency)
    pk += 1

# Open the file in write mode
with open("currencies_db_data.json", "w") as outfile:
    # Dump the list of dictionaries to the JSON file
    json.dump(currencies, outfile, indent=4)  # Indent for readability

print("Currencies converted to currencies_db_data.json successfully!")
