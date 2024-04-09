from src.masks import masc_of_bill, masc_of_card


def masks_of_cards(data: str) -> str:
    """ "
    Функция переиспользует ранее написанные функции и возвращает исходную строку с замаскированным номером карты/счета.
    """
    redact_data = data.split(" ")
    if redact_data[0] != "Счет":
        return f'{" ".join(redact_data[:-1])} {masc_of_card(redact_data[-1])}'
    return f"Счет {masc_of_bill(redact_data[-1])}"


def give_data(time: str) -> str:
    """
    Принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    redact_time = time.split("T")[0].split("-")
    return f"{redact_time[2]}.{redact_time[1]}.{redact_time[0]}"

