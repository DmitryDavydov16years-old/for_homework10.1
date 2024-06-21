import re
from collections import Counter


def _for_first(my_dicts, need):
    counter = []
    pattern = re.compile(rf'{need}')
    for i in my_dicts:
        right_or_no = pattern.search(i['description'])
        if right_or_no == None:
            continue
        else:
            counter.append(i)
    return counter


def _for_second(my_dicts, need):
    my_list = []
    for i in my_dicts:
        for key, value in need.items():
            if type(value) == str:
                pattern = re.compile(rf'{value}')
                right_or_no = pattern.search(i['description'])
                if right_or_no != None:
                    my_list.append(key)
            if type(value) == list:
                for gh in value:
                    pattern = re.compile(rf'{gh}')
                    right_or_no = pattern.search(i['description'])
                    if right_or_no != None:
                        my_list.append(key)
    return Counter(my_list)


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
print(_for_second(transactions_, categories_))
