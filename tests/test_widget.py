import pytest

from src.widget import changes_date_line, masking_card_or_account


@pytest.fixture
def test_data() -> str:
    return "Счет 73654108430135874305"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-08-11T02:26:18.691407", "11.08.2018"),
        ("2016-09-14T02:26:18.691407", "14.09.2016"),
        ("2019-11-29T02:26:18.691407", "29.11.2019"),
    ],
)
def test_changes_date_line(string: str, expected_result: str) -> None:
    assert changes_date_line(string) == expected_result


def test_masking_card_or_account(test_data: str) -> None:
    assert masking_card_or_account(test_data) == "Счет **4305"
