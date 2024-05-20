from typing import List

from src.logger import setup_logging

logger = setup_logging()


# Я напишу здесь каку-нибудь функцию, чтоб тут был не только лог
def plusOne(digits: List[int]) -> List[int]:
    """
    Функция принимает целое чсило в виде целочисленного массива цифр,
    увеличвает это целое число на единицу и возвращает полученный массив цифр.
    """

    numbers = []
    for number in digits:
        numbers.append(str(number))
    increased_number = int("".join(numbers)) + 1
    new_array = []
    for number in str(increased_number):
        new_array.append(int(number))
    logger.info("Все в порядке")
    return new_array
