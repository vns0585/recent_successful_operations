from datetime import datetime

from src import masks


def mask_account_card(account_type_and_number: str | None) -> str:
    """Маскировка информации о счетах и картах в строке"""

    if account_type_and_number is None:
        return ""

    substrings = account_type_and_number.split()
    if len(substrings) < 2:  # Проверяем не пусты ли подстроки с типом и номером счета
        raise ValueError("Подстроки с типом или номером счета/карты пусты.")

    account_number = substrings[-1]
    if not account_number.isdigit() or len(account_number) < 4:  # Проверяем корректность данных номера счета
        raise ValueError("Номер счета/карты некорректен.")

    # Собираем название типа счета, если в нем были символы пробела
    account_type = ""
    for i in range(len(substrings) - 1):
        if substrings[i].isalpha():  # в типе счета не должно быть цифр
            account_type += substrings[i] + " "
        else:
            raise ValueError("В типе счета не должно быть цифр.")

    # Маскировка в зависимости от типа счета
    if account_type[:4].lower() == "счет" or account_type[:4].lower() == "счёт":
        return f"{account_type}{masks.get_mask_account(account_number)}"
    else:
        if len(account_number) != 16:
            raise ValueError("Номер карты некорректен.")
        return f"{account_type}{masks.get_mask_card_number(account_number)}"


def get_date(date: str | None) -> str:
    """Принимает строку с датой в iso-формате и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if date is None:
        return ""
    try:
        return datetime.fromisoformat(date).strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты.")
