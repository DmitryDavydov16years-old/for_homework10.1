import os.path
from typing import Any
from unittest.mock import patch

from pandas import DataFrame

from src.read_excel_and_csv_file import read_csv_file, read_xlsx_file


@patch('pandas.read_csv')
def test_read_csv_file(mock_read: Any) -> None:
    mock_read.return_value = DataFrame({'52': ['52', '42']})
    assert read_csv_file(os.path.join('..', 'data', 'transactions.csv')) == [{'52': '52'}, {'52': '42'}]


@patch('pandas.read_excel')
def test_read_xlsx_file(mock_read: Any) -> None:
    mock_read.return_value = DataFrame({'49': ['49']})
    assert read_xlsx_file(os.path.join('..', 'data', 'transactions_excel.csv')) == [{'49': '49'}]
