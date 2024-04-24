from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions

descriptions = transaction_descriptions(transactions)
currency = filter_by_currency(transactions, "USD")
cards = card_number_generator(1, 5)


def test_transaction_descriptions() -> None:
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


def test_filter_by_currency() -> None:
    assert next(currency)["id"] == 939719570
    assert next(currency)["id"] == 142264268
    assert next(currency)["id"] == 895315941


def test_card_number_generator() -> None:
    assert next(cards) == "0000 0000 0000 0001"
    assert next(cards) == "0000 0000 0000 0002"
    assert next(cards) == "0000 0000 0000 0003"
    assert next(cards) == "0000 0000 0000 0004"
    assert next(cards) == "0000 0000 0000 0005"
