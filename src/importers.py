from functools import wraps
from typing import Any, Callable

import pandas as pd


def prepare_transactions(df: pd.DataFrame) -> list:
    """Подготовка транзакций из DataFrame для использования в проекте."""
    try:

        df["id"] = pd.to_numeric(df["id"], errors='coerce').astype('Int64')
        df["id"] = df["id"].where(pd.notna(df["id"]), None)
        df["date"] = pd.to_datetime(df["date"], errors='coerce').dt.strftime("%Y-%m-%dT%H:%M:%S.%f")
        df["amount"] = pd.to_numeric(df["amount"], errors='coerce').astype('str').replace('nan', None)
        df = df.astype(object).where(pd.notna(df), None)
        return [
            {
                "id": item["id"],
                "state": item["state"],
                "date": item["date"],
                "operationAmount":
                    {
                        "amount": item["amount"],
                        "currency":
                            {
                                "name": item["currency_name"],
                                "code": item["currency_code"]
                            }
                    },
                "description": item["description"],
                "from": item["from"],
                "to": item["to"]
            } for item in df.to_dict(orient='records')
        ]
    except KeyError:
        raise KeyError("Отсутствует колонка с данными.")
    except (ValueError, TypeError):
        raise Exception("Ошибка подготовки транзакций.")
    except AttributeError:
        raise AttributeError("Некорректный тип данных.")
    except Exception:
        raise Exception("Ошибка подготовки транзакций.")


def import_errors(func: Callable) -> Callable:
    """Декоратор для обработки ошибок импорта."""
    @wraps(func)
    def wrapper(*args: str, **kwargs: str) -> Any:
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден.")
        except pd.errors.EmptyDataError:
            return []
        except Exception:
            raise Exception("Ошибка при импорте.")
    return wrapper


@import_errors
def import_from_csv(filename: str) -> list:
    """Импорт транзакций из CSV файла."""
    return prepare_transactions(pd.read_csv(filename, delimiter=';'))


@import_errors
def import_from_excel(filename: str) -> list:
    """Импорт транзакций из Excel файла."""
    return prepare_transactions(pd.read_excel(filename))
