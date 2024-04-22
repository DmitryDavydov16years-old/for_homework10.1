def sorting_the_dictionary(list_of_dictionaries: list, value_for_key: str = "EXECUTED") -> list:
    """
    функция принимает на вход список словарей и значение для
    ключа state (опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение.
    """
    modified_dictionary = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == value_for_key:
            modified_dictionary.append(dictionary)
    return modified_dictionary


def sorting_by_date(list_of_dictionaries: list, reverse: bool = True) -> list:
    """ "
    Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).
    """
    sorting = sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse)
    return sorting
