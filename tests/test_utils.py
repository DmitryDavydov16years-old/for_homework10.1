import json
from unittest.mock import patch

from src.utils import dictionaries_financial_transaction_data, returns_transaction_amount

for_example = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612",
}


@patch("requests.get")
def test_returns_transaction_amount(mock_get):
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 90}}
    assert (
            returns_transaction_amount(
                {
                    "id": 667307132,
                    "state": "EXECUTED",
                    "date": "2019-07-13T18:51:29.313309",
                    "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "USD"}},
                    "description": "Перевод с карты на счет",
                    "from": "Maestro 1308795367077170",
                    "to": "Счет 96527012349577388612",
                }
            )
            == 8806847.4
    )


def test_dictionaries_financial_transaction_data():
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(for_example)
        assert dictionaries_financial_transaction_data("../data/operations.json") == for_example
        mock_open.assert_called_once_with("../data/operations.json", "r", encoding="UTF-8")
