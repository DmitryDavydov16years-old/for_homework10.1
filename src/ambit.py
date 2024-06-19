from typing import Any

import pandas as pd


def read_csv_file(filename: str) -> Any:
    """Читает файл csv типа и возвращает словарь"""
    with open(filename, encoding="UTF-8") as file:
        data = pd.read_csv(filename)
        return data.to_dict("records")


def read_xlsx_file(filename: str) -> Any:
    """Читает файл xlsx типа и возвращает словарь """
    data = pd.read_excel(filename)
    return data.to_dict("records")
