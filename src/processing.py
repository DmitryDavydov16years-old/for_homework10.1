def sorting_the_dictionary(list_of_dictionaries: list, value_for_key: str = "EXECUTED") -> list:
    modified_dictionary = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == value_for_key:
            modified_dictionary.append(dictionary)
    return modified_dictionary


def sorting_by_date(list_of_dictionaries: list, reverse: bool = True) -> list:
    sorting = sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse)
    return sorting
