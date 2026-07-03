import masks
from typing import Union


def mask_account_card(account_type_and_number: str) -> Union[str, None]:
    """Маскировка информации о счетах и картах в строке"""

    substrings = account_type_and_number.split()
    if not 2 <= len(substrings) <= 3:
        return None

    if substrings[0].lower() == "счет" or substrings[0].lower() == "счёт":
        if not substrings[-1].isdigit() or len(substrings[-1]) < 4:
            return None
        substrings[-1] = masks.get_mask_account(substrings[-1])
    else:
        if not substrings[0].isalpha() or not substrings[-1].isdigit() or not substrings[-2].isalpha() or len(substrings[-1]) != 16:
            return None
        substrings[-1] = masks.get_mask_card_number(substrings[-1])

    return " ".join(substrings)


def get_date(date: str) -> Union[str, None]:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if len(date) < 10 or not date[:4].isdigit() or not date[5:7].isdigit() or not date[8:10].isdigit() or date[4] != "-" or date[7] != "-":
        return None
    return ".".join(date[:10].split("-")[::-1])


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
