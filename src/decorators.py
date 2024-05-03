import time
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable:
    """
    Декоратор, логирующий вызов функции и ее результат
    """

    def wrapper(func: Callable) -> Callable:
        """
        Обертка для декорируемой функции
        """

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """
            Выполняент логирование
            """
            if filename:
                with open(filename, "a") as file:
                    current_time = time.time()

                    time_struct = time.localtime(current_time)

                    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
                    try:
                        func(*args, **kwargs)
                    except Exception as e:
                        file.write(f"\n{formatted_time} my_function error{type(e).__name__}. Inputs: {args} {kwargs}")
                        return f"{type(e).__name__}"
                    else:
                        file.write(f"\n{formatted_time} my_function ok")
                        return f"{formatted_time} my_function ok"
            else:
                current_time = time.time()

                time_struct = time.localtime(current_time)

                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
                print(func(*args, **kwargs))
                return f"{formatted_time} my_function ok"

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y
