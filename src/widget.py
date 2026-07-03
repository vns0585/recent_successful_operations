from datetime import datetime
from typing import Union

import masks


def mask_account_card(account_type_and_number: str) -> Union[str, None]:
    """Маскировка информации о счетах и картах в строке"""

    substrings = account_type_and_number.split()
    if len(substrings) < 2:  # Проверяем не пусты ли подстроки с типом и номером счета
        return None

    account_number = substrings[-1]
    if not account_number.isdigit() or len(account_number) < 4:  # Проверяем корректность данных номера счета
        return None

    # Собираем название типа счета, если в нем были символы пробела
    account_type = ""
    for i in range(len(substrings) - 1):
        if substrings[i].isalpha():  # в типе счета не должно быть цифр
            account_type += substrings[i] + " "
        else:
            return None

    # Маскировка в зависимости от типа счета
    if account_type[:4].lower() == "счет" or account_type[:4].lower() == "счёт":
        return f"{account_type}{masks.get_mask_account(account_number)}"
    else:
        if len(account_number) != 16:
            return None
        return f"{account_type}{masks.get_mask_card_number(account_number)}"


def get_date(date: str) -> Union[str, None]:
    """Принимает строку с датой в iso-формате и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    try:
        return datetime.fromisoformat(date).strftime("%d.%m.%Y")
    except ValueError:
        return None


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))

    print(get_date("2024-03-11T02:26:18.671407"))
