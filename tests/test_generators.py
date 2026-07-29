from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions: list[dict], transactions_usd: list[dict]) -> None:
    assert list(filter_by_currency(transactions, "USD")) == transactions_usd


def test_filter_by_currency_rub(transactions: list[dict], transactions_rub: list[dict]) -> None:
    assert list(filter_by_currency(transactions, "RUB")) == transactions_rub


def test_filter_by_currency_no_transactions_eur(transactions: list[dict]) -> None:
    assert list(filter_by_currency(transactions, "EUR")) == []


@pytest.mark.parametrize(
    "wrong_transactions, wrong_currency",
    [
        (1, "USD"),
        ("USD", "USD"),
        ([], []),
        ([1, 2], "USD"),
        (["USD", "USD"], "USD"),
        ({}, "USD"),
        ([], 1),
        ([], {}),
    ],
)
def test_filter_by_currency_wrong_params(wrong_transactions: Any, wrong_currency: Any) -> None:
    with pytest.raises(TypeError):
        list(filter_by_currency(wrong_transactions, wrong_currency))


def test_transaction_descriptions(transactions: list[dict], transactions_description: list[str]) -> None:
    assert list(transaction_descriptions(transactions)) == transactions_description


@pytest.mark.parametrize(
    "wrong_transaction",
    [
        [{}],
        [{"a": "b"}],
    ],
)
def test_transaction_descriptions_void_description(wrong_transaction: Any) -> None:
    assert list(transaction_descriptions(wrong_transaction)) == [""]


@pytest.mark.parametrize(
    "wrong_transaction",
    [
        1,
        "2",
        {},
        [],
    ],
)
def test_transaction_descriptions_wrong_params(wrong_transaction: Any) -> None:
    with pytest.raises(TypeError):
        list(transaction_descriptions(wrong_transaction))


def test_card_number_generator() -> None:
    result = card_number_generator(1, 5)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
    assert next(result) == "0000 0000 0000 0003"
    assert next(result) == "0000 0000 0000 0004"
    assert next(result) == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, "0000 0000 0000 0001"),
        (15001, 15001, "0000 0000 0001 5001"),
        (1234567891012151, 1234567891012151, "1234 5678 9101 2151"),
        (0, 0, "0000 0000 0000 0000"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
    ],
)
def test_card_number_generator_one_card(start: int, stop: int, expected: str) -> None:
    assert next(card_number_generator(start, stop)) == expected


@pytest.mark.parametrize(
    "start, stop",
    [
        (1, "2"),
        (2.5, 9),
        ([], 10),
    ],
)
def test_card_number_generator_wrong_type_params(start: Any, stop: Any) -> None:
    with pytest.raises(TypeError):
        next(card_number_generator(start, stop))


@pytest.mark.parametrize(
    "start, stop",
    [
        (-1, 4),
        (2, -9),
        (11111111111111111, 10),
        (0, 11111111111111111),
    ],
)
def test_card_number_generator_wrong_value_params(start: int, stop: int) -> None:
    with pytest.raises(ValueError):
        next(card_number_generator(start, stop))


def test_card_number_generator_mixed_up_params() -> None:
    assert list(card_number_generator(2, 1)) == ["0000 0000 0000 0001", "0000 0000 0000 0002"]
