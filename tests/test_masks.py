

import pytest

from src.masks import masking_account, masking_card


@pytest.fixture
def test_data() -> str:
    return "7000792289606361"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("73654108438137874307", "**4307"),
        ("73654108438137874507", "**4507"),
        ("73654108438137874517", "**4517"),
    ],
)
def test_masking_account(string: str, expected_result: str) -> None:
    assert masking_account(string) == expected_result


def test_masking_card(test_data: str) -> None:
    assert masking_card(test_data) == "7000 79**  **** 6361"
