import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("1234567891112130", "1234 56** **** 2130"),
        (1234567891112130, "1234 56** **** 2130"),
    ],
)
def test_get_mask_card_number(card_number: str | int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "",
        "70007922896063610",
        70007922896063610,
        "700079228960636",
        700079228960636,
        "7",
        6,
        700079228960636648395673839,
        "700079228960636648395673839",
        "qwertyuiopasdfgh",
        "12345789qwerty0",
        "ughdfgh",
        "qwertyuiopasdfghjklzxcvbnm",
    ],
)
def test_get_mask_card_number_with_invalid_card_number(card_number: str | int) -> None:
    with pytest.raises(ValueError) as e:
        get_mask_card_number(card_number)
    assert e.value.args[0] == "Неверный формат номера карты. Ожидается номер карты длинной 16 цифр."


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("123456789", "**6789"),
        (123456789, "**6789"),
        ("1234", "**1234"),
        (1234, "**1234"),
    ],
)
def test_get_mask_account(account_number: str | int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", ["", "1", 1, "12", 12, "123", 123, "sffdf", "12a345678"])
def test_get_mask_account_with_invalid_account_number(account_number: str | int) -> None:
    with pytest.raises(ValueError) as e:
        get_mask_account(account_number)
    assert e.value.args[0] == "Неверный формат номера счета. Ожидается номер счета длинной от 4 цифр."
