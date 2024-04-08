from src.masks import masc_of_bill, masc_of_card


def masks_of_cards(data: str) -> str:
    """ "
    Функция переиспользует ранее написанные функции
    и возвращает исходную строку с замаскированным номером карты/счета.
    """
    right_data = data.split(" ")
    if right_data[0] == "Счет":
        return f"Счет {masc_of_bill(right_data[-1])}"
    else:
        return f'{" ".join(right_data[:-1])} {masc_of_card(right_data[-1])}'


def right_data(time: str) -> str:
    """
    Принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    right = time.split("T")[0].split("-")
    return f"{right[2]}.{right[1]}.{right[0]}"
