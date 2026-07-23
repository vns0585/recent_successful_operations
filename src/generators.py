from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    return filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction["description"]
