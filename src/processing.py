import re
from collections import Counter


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Возвращает новый список, содержащий только те словари, у которых ключ state соответствует."""
    try:
        return [item for item in list_of_dict if item.get("state") == state]
    except KeyError:
        raise KeyError("В переданных словарях отсутствует ключ 'state'.")
    except TypeError:
        raise TypeError("В списке данные неверного типа. Ожидаются словари.")


def sort_by_date(list_of_dict: list, descending: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате (ключ date), в указанном порядке."""
    try:
        return sorted(list_of_dict, key=lambda item: item["date"], reverse=descending)
    except KeyError:
        raise KeyError("В переданных словарях отсутствует ключ 'date'.")
    except TypeError:
        raise TypeError("В списке данные неверного типа. Ожидаются словари.")


def process_bank_search(data: list[dict], search: str | None) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    if search is None:
        return []
    return [item for item in data if re.search(search, str(item.get("description")), re.IGNORECASE)]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории."""
    descriptions = [str(item.get("description")).lower() for item in data if not item.get("description") is None]
    return {category: Counter(descriptions).get(category.lower()) for category in categories}
