from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    return filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)
