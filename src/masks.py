import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def masking_card(cards: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    with open("example.log", "w") as file:
        file.write("")
    logger.info('Все работает')
    return f"{cards[:4]} {cards[4:6]}**  **** {cards[-4:]}"


def masking_account(cards: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    with open("example.log", "w") as file:
        file.write("")
    logger.info('Все работает')
    return f"**{cards[-4:]}"
