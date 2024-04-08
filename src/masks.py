def masc_of_card(cards: str) -> str:
    """ "
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    return f"{cards[:4]} {cards[4:6]}**  **** {cards[-4:]}"


def masc_of_bill(cards: str) -> str:
    """ "
    Функция принимает на вход номер счета и возвращает его маску.
    """
    return f"**{cards[-4:]}"
