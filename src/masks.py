import logging
import os
from typing import Union

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер банковской карты, длинной 16 цифр, в формате XXXX XX** **** XXXX, где X — это цифра номера."""

    card_number_str = str(card_number)
    logger.debug(f"Получен номер карты: {card_number_str}")

    if len(card_number_str) != 16 or not card_number_str.isdigit():
        logger.error("Неверный формат номера карты. Ожидается номер карты длинной 16 цифр.")
        raise ValueError("Неверный формат номера карты. Ожидается номер карты длинной 16 цифр.")

    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.debug(f"Номер карты замаскирован: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Маскирует номер банковского счета, длинной от 4 цифр, в формате **XXXX, где X — это цифра номера."""

    account_number_str = str(account_number)
    logger.debug(f"Получен номер счета: {account_number_str}")

    if len(account_number_str) < 4 or not account_number_str.isdigit():
        logger.error("Неверный формат номера счета. Ожидается номер счета длинной от 4 цифр.")
        raise ValueError("Неверный формат номера счета. Ожидается номер счета длинной от 4 цифр.")

    masked_account_number = f"**{account_number_str[-4:]}"
    logger.debug(f"Номер счета замаскирован: {masked_account_number}")
    return masked_account_number
