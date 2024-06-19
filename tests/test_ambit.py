import os.path
from unittest.mock import patch

from pandas import DataFrame

from src.ambit import read_csv_file


@patch('pandas.read_csv')
def test_read_csv_file(mock_read) -> None:
    mock_read.return_value = DataFrame({'1': ['1']})
    assert read_csv_file(os.path.join('..', 'data', 'transactions.csv')) == [{'1': '1'}]
