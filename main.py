from typing import Tuple, List, Dict, Any

from src.filter import filter_by_line
from src.processing import sorting_the_dictionary, sorting_by_date
from src.read_excel_and_csv_file import read_csv_file, read_xlsx_file
from src.utils import finding_dictionaries_with_financial_transaction_data
from src.widget import changes_date_line, masking_card_or_account

first_text = """Привет! Добро пожаловать в программу работы с банковскими транзакициями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
"""
second_text = "Для обработки выбран json файл."
third_text = """Введите статус по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
fourth_text = """Введите статус по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
fivth_text = """Введите статус по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""


def print_about_first() -> Tuple[List[Dict[str, Any]], int]:
    user_choice = input(first_text)
    if user_choice == '1':
        print("Для обработки выбран json")
        json_data = finding_dictionaries_with_financial_transaction_data("data/operations.json")
        return json_data, 1
    if user_choice == '2':
        print("Для обработки выбран csv файл.")
        csv_data = read_csv_file("data/transactions.csv")
        return csv_data, 2
    if user_choice == '3':
        print("Для обработки выбран xlsx файл.")
        xlsx_data = read_xlsx_file("data/transactions_excel.xlsx")
        return xlsx_data, 3
    return [], 0


def print_about_second(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    status_filter = input(third_text)
    if status_filter == "EXECUTED":
        return sorting_the_dictionary(data)
    if status_filter == "CANCELED":
        return sorting_the_dictionary(data, "CANCELED")
    if status_filter == "PENDING":
        return sorting_the_dictionary(data, "PENDING")
    return data


def print_about_third(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    sort_choice = input("Отсортировать операции по дате? Да/Нет")
    if sort_choice.lower() == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?")
        if sort_order.lower() == "по убыванию":
            return sorting_by_date(data)
        if sort_order.lower() == "по возрастанию":
            return sorting_by_date(data, reverse=False)
    return data


def about_ruble(data: List[Dict[str, Any]], number: int) -> List[Dict[str, Any]]:
    ruble_only = input('Выводить только рублевые транзакции? Да/Нет')
    if ruble_only.lower() == "да":
        if number in [2, 3]:
            return [transaction for transaction in data if transaction["currency_code"] == "RUB"]
        if number == 1:
            return [transaction for transaction in data if transaction["operationAmount"]["currency"]["code"] == "RUB"]
    return data


def filter_by_word(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    filter_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if filter_choice.lower() == "да":
        user_answer = input("Введите это слово")
        print("Распечатываю итоговый список транзакций...")
        return filter_by_line(data, user_answer)
    print("Распечатываю итоговый список транзакций...")
    return data


def make_beautiful_answer(data: List[Dict[str, Any]], number: int) -> None:
    if number == 1:
        print(f"Всего банковских операций в выборке: {len(data)}")
        for transaction in data:
            if transaction['description'] == "Открытие вклада":
                print(f"""
    {changes_date_line(transaction['date'])} {transaction['description']}
    {masking_card_or_account(transaction['to'])}
    Сумма: {transaction["operationAmount"]["amount"]}{transaction['operationAmount']['currency']["code"]}""")
            else:
                print(f"""
    {changes_date_line(transaction['date'])} {transaction['description']}
    {masking_card_or_account(transaction["from"])} -> {masking_card_or_account(transaction["to"])}
    Сумма: {transaction["operationAmount"]["amount"]}{transaction['operationAmount']['currency']["code"]}""")
    elif number in [2, 3]:
        print(f"Всего банковских операций в выборке: {len(data)}")
        for transaction in data:
            if transaction['description'] == "Открытие вклада":
                print(f"""
        {changes_date_line(transaction['date'])} {transaction['description']}
        {masking_card_or_account(transaction['to'])}
        Сумма: {transaction["amount"]}{transaction['currency_code']}""")
            else:
                print(f"""
        {changes_date_line(transaction['date'])} {transaction['description']}
        {masking_card_or_account(transaction["from"])} -> {masking_card_or_account(transaction["to"])}
        Сумма: {transaction["amount"]}{transaction['currency_code']}""")


def main() -> None:
    data, number = print_about_first()
    if not data:
        print("Неверный выбор. Завершение программы.")
        return
    data_first = print_about_second(data)
    data_second = print_about_third(data_first)
    data_third = about_ruble(data_second, number)
    data_fourth = filter_by_word(data_third)
    make_beautiful_answer(data_fourth, number)


main()
