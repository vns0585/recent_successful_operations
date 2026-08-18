import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_account_number: str, expected: str) -> None:
    assert mask_account_card(card_account_number) == expected


@pytest.mark.parametrize("card_account_number", ["", "1596837868705199", "Maestro"])
def test_mask_account_card_with_void_params(card_account_number: str) -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card(card_account_number)
    assert e.value.args[0] == "Подстроки с типом или номером счета/карты пусты."


@pytest.mark.parametrize("card_account_number", ["Maestro 123", "Maestro qwerty"])
def test_mask_account_card_with_invalid_number(card_account_number: str) -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card(card_account_number)
    assert e.value.args[0] == "Номер счета/карты некорректен."


@pytest.mark.parametrize(
    "card_account_number",
    ["Maestro1 1596837868705199", "Mae5tro 1596837868705199", "0isa Classic 6831982476737658", "123 6831982476737658"],
)
def test_mask_account_card_with_invalid_card_account_number(card_account_number: str) -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card(card_account_number)
    assert e.value.args[0] == "В типе счета не должно быть цифр."


@pytest.mark.parametrize(
    "card_account_number",
    [
        "Maestro 12345",
        "Visa Classic 6831982476737658822215332",
        "Visa Classic 68319824767376581",
        "Visa Classic 683198247673765",
    ],
)
def test_mask_account_card_with_invalid_card_number(card_account_number: str) -> None:
    with pytest.raises(ValueError) as e:
        mask_account_card(card_account_number)
    assert e.value.args[0] == "Номер карты некорректен."


def test_mask_account_card_none() -> None:
    assert mask_account_card(None) == ""


@pytest.mark.parametrize(
    "date_in_isoformat, expected",
    [
        ("2026-07-16T11:44:00.000000", "16.07.2026"),
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T04:16:12.571707", "01.01.2020"),
    ],
)
def test_get_date(date_in_isoformat: str, expected: str) -> None:
    assert get_date(date_in_isoformat) == expected


@pytest.mark.parametrize(
    "date_in_isoformat",
    ["", "026-07-16T11:44:00.000000", "2024-03-11T02:2618", "2020-01-0104:16:12.571707"],
)
def test_get_date_with_invalid_isoformat(date_in_isoformat: str) -> None:
    with pytest.raises(ValueError) as e:
        get_date(date_in_isoformat)
    assert e.value.args[0] == "Некорректный формат даты."


def test_get_date_none() -> None:
    assert get_date(None) == ""

