from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Вход: список словарей (транзакции). Выход: итератор, выдающий транзакции, где валюта операции соответствует"""
    if not isinstance(transactions, list) or not all(isinstance(item, dict) for item in transactions):
        raise TypeError("Неверный формат транзакций. Ожидается список словарей.")
    if not isinstance(currency, str):
        raise TypeError("Неверный формат валюты. Ожидается строка.")
    return filter(lambda t: t.get("operationAmount", {}).get("currency", {}).get("code") == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if (
        not isinstance(transactions, list)
        or not all(isinstance(item, dict) for item in transactions)
        or not transactions
    ):
        raise TypeError("Неверный формат транзакций. Ожидается список словарей.")
    for transaction in transactions:
        if transaction.get("description") is None:
            yield ""
        else:
            yield str(transaction.get("description"))


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт из заданного диапазона в формате XXXX XXXX XXXX XXXX (X — цифра номера)."""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Параметры функции должны быть целыми числами.")
    if start > stop:
        start, stop = stop, start
    if len(str(stop)) > 16 or stop < 0 or start < 0:
        raise ValueError("Переданные значения вне диапазона возможных номеров карт.")
    for value in range(start, stop + 1):
        card_number = f"{str(value):0>16}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
