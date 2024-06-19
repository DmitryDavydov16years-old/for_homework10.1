from src.logger import setup_logging

logger = setup_logging()


def masking_card(cards: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    logger.info("Все работает")
    return f"{cards[:4]} {cards[4:6]}**  **** {cards[-4:]}"


def masking_account(cards: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    logger.info("Все работает")
    return f"**{cards[-4:]}"


def open_f(file_path):
    with open(file_path, 'r', encoding="UTF8") as f:
        return f.readlines()



