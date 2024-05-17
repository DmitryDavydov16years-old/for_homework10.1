import json
from typing import Any
from unittest.mock import patch

from src.utils import finding_dictionaries_with_financial_transaction_data, finding_transaction_amount

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
def test_finding_dictionaries_with_financial_transaction_data(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 90}}
    assert (
            finding_transaction_amount(
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


def test_dictionaries_financial_transaction_data() -> None:
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(for_example)
        assert finding_dictionaries_with_financial_transaction_data("../data/operations.json") == for_example
        mock_open.assert_called_once_with("../data/operations.json", "r", encoding="UTF-8")
