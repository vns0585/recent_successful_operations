from functools import wraps
from typing import Any, Callable


def log(filename: str = '') -> Callable:
    """Автоматически логирует начало и конец выполнения функции, а также результаты или возникшие ошибки."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not isinstance(filename, str):
                raise TypeError("Имя файла должно быть строкового типа")
            message = str(func.__name__)
            status = ""
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                error = err
            else:
                status = "Ok"
            if status == "Ok":
                message += f" {status}"
            else:
                message += f" error: {error}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, 'a', encoding="utf-8") as file:
                    file.write(f"{message}\n")
            else:
                print(message)
            if status == "Ok":
                return result
            else:
                raise error
        return wrapper
    return decorator
