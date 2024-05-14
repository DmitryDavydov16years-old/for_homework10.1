import json
import os

import requests
from dotenv import load_dotenv

API_KEY = os.getenv("api_keys")
load_dotenv()


def dictionaries_financial_transaction_data(path_to_file):
    try:
        with open(path_to_file, "r", encoding='UTF-8') as file:
            data = json.load(file)
    except Exception:
        return []
    else:
        return data


value = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
        "amount": "97853.86",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
}


def returns_transaction_amount(tranzaction):
    currency_of_tranzaction = tranzaction["operationAmount"]["currency"]["code"]
    url = f"https://v6.exchangerate-api.com/v6/0504d3f7601436eb90528abf/latest/{currency_of_tranzaction}"
    response = requests.get(url, headers={"apikey": API_KEY})
    response_data = json.loads(response.text)
    return float(tranzaction["operationAmount"]["amount"]) * response_data["conversion_rates"]["RUB"]



