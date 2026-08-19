import re
from collections import Counter


def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list:
    """Возвращает новый список, содержащий только те словари, у которых ключ state соответствует."""
    try:
        return [item for item in list_of_dict if item.get("state") == state]
    except AttributeError:
        raise AttributeError("В списке данные неверного типа. Ожидаются словари.")


def sort_by_date(list_of_dict: list[dict], descending: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате (ключ date), в указанном порядке."""
    for item in list_of_dict:
        if not type(item) is dict:
            raise AttributeError("В списке данные неверного типа. Ожидаются словари.")
    return sorted(list_of_dict, key=lambda item: item.get("date") or "", reverse=descending)


def process_bank_search(data: list[dict], search: str | None) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    if search is None:
        return []
    return [item for item in data if re.search(search, item.get("description") or "", re.IGNORECASE)]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории."""
    descriptions = [str(item.get("description")).lower() for item in data if not item.get("description") is None]
    return {category: Counter(descriptions).get(category.lower()) for category in categories}
