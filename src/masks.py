from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер банковской карты, длинной 16 цифр, в формате XXXX XX** **** XXXX, где X — это цифра номера."""

    card_number_str = str(card_number)

    if len(card_number_str) != 16 or not card_number_str.isdigit():
        return "Ошибка: Неверный формат номера карты. Ожидается номер карты длинной 16 цифр."

    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Маскирует номер банковского счета, длинной от 4 цифр, в формате **XXXX, где X — это цифра номера."""

    account_number_str = str(account_number)

    if len(account_number_str) < 4 or not account_number_str.isdigit():
        return "Ошибка: Неверный формат номера счета. Ожидается номер счета длинной от 4 цифр."

    return f"**{account_number_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))

    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
