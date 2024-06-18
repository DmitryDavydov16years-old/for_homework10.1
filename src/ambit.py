import pandas as pd


def read_csv_file(filename, delimeter=";"):
    with open(filename, encoding="UTF-8") as file:
        data = pd.read_excel(file)
        return data.to_dict("records")


def read_xlsx_file(filename: str):
    """Читает file xlsx и возвращает словарь """
    data = pd.read_excel(filename)
    return data.to_dict("records")


print(read_csv_file("../data/transactions.csv"))
