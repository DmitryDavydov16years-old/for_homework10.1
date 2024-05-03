import time

from src.decorators import my_function

current_time = time.time()

time_struct = time.localtime(current_time)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)


def test_my_function_1() -> None:
    """
    Функция тестирует декоратор
    """
    my_function(1, 3)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()

        assert f"{formatted_time} my_function ok" == lines[-1]


def test_my_function() -> None:
    """
    Функция тестирует декоратор
    """
    calling_my_function = my_function(1, 3)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()

        assert calling_my_function == lines[-1]
