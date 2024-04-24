from typing import Iterator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def transaction_descriptions(transaction: list[dict]) -> Iterator[str]:
    """ "
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    """
    for data in transaction:
        yield data["description"]


def filter_by_currency(transaction: list[dict], currency: str) -> Iterator[dict]:
    """ "
    Функция, которая принимает список словарей (или объект, который выдает по одной словари с транзакциями),
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for data in transaction:
        if data["operationAmount"]["currency"]["code"] == currency:
            yield data


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """ "
    Генератор номеров банковских карт, который должен генерировать номера карт в формате "XXXX XXXX XXXX XXXX",
    где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например,
    от 0000 0000 0000 0001 до 9999 9999 9999 9999 (диапазоны передаются как параметры генератора).
    """
    for number in range(start, end + 1):
        list_with_numbers = []
        number_of_zeros = 16 - len(str(number))
        for numbers in range(number_of_zeros):
            list_with_numbers.append("0")
        for data in str(number):
            list_with_numbers.append(data)

        first_part = "".join(list_with_numbers[:4])
        second_part = "".join(list_with_numbers[4:8])
        third_part = "".join(list_with_numbers[8:12])
        fourth_part = "".join(list_with_numbers[12:17])
        yield f"{first_part} {second_part} {third_part} {fourth_part}"
