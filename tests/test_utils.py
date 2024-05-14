from unittest.mock import Mock
from unittest.mock import patch
import requests
import json

value = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
]


# def test_returns_transaction_amount():
#     with patch('requests.get') as mock_get:
#         mock_get.return_value.json.return_value = '97853.86'
#         assert returns_transaction_amount(value) == '97853.86'
#         mock_get.assert_called_once_with(value)

def dictionaries_financial_transaction_data(path_to_file):
    try:
        with open(path_to_file, "r", encoding='UTF-8') as file:
            data = json.load(file)
    except Exception:
        return []
    else:
        return data


def test_dictionaries_financial_transaction_data():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = value
        assert dictionaries_financial_transaction_data('../data/operations.json') == value
