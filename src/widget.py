import masks


def mask_account_card(account_type_and_number: str) -> str:
    """Маскировка информации о счетах и картах в строке"""
    account = account_type_and_number.split()
    if account[0].lower() == "счет" or account[0].lower() == "счёт":
        account[-1] = masks.get_mask_account(account[-1])
    else:
        account[-1] = masks.get_mask_card_number(account[-1])
    return " ".join(account)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))