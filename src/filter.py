import re
from collections import Counter
from typing import List, Dict, Any


def filter_by_line(dicts: List[Dict[str, Any]], required_line: str) -> List[Dict[str, Any]]:
    filtered_dicts = []
    pattern = re.compile(rf'{required_line}')
    for dictionary in dicts:
        match = pattern.search(dictionary['description'])
        if match is not None:
            filtered_dicts.append(dictionary)
    return filtered_dicts


def counting_number_different_operations(dicts: List[Dict[str, Any]], patterns: Dict[str, Any]) -> Counter:
    matched_keys = []
    for dictionary in dicts:
        for key, value in patterns.items():
            if isinstance(value, str):
                pattern = re.compile(rf'{value}')
                if pattern.search(dictionary['description']) is not None:
                    matched_keys.append(key)
            elif isinstance(value, list):
                for item in value:
                    pattern = re.compile(rf'{item}')
                    if pattern.search(dictionary['description']) is not None:
                        matched_keys.append(key)
    return Counter(matched_keys)


transactions_ = [
    {"description": "oплата за интернет"},
    {"description": "Покупка продуктов в магазине"},
    {"description": "Перевод денег другу"},
    {"description": "Оплата за мобильную связь"},
    {"description": "Покупка билетов на концерт"},
]

categories_ = {
    "Интернет": "oплата",
    "Продукты": "продукты",
    "Другое": "Перевод"
}
