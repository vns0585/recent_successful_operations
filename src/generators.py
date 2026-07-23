from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    return filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_value: int, stop_value: int) -> Iterator[str]:
    if not isinstance(start_value, int) or not isinstance(stop_value, int):
        raise TypeError("Параметры функции должны быть целыми числами.")
    if start_value > stop_value:
        start_value, stop_value = stop_value, start_value
    if len(str(stop_value)) > 16 or stop_value < 0 or start_value < 0:
        raise ValueError("Переданные значения вне диапазона возможных номеров карт.")
    for value in range(start_value, stop_value + 1):
        card_number = f"{str(value):X>16}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
