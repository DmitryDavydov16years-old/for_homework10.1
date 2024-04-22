def masking_card(cards: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    return f"{cards[:4]} {cards[4:6]}**  **** {cards[-4:]}"


def masking_account(cards: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    return f"**{cards[-4:]}"
