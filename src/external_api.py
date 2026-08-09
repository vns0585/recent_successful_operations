import os

import requests
from dotenv import load_dotenv

URL = "https://api.apilayer.com/exchangerates_data/convert"

load_dotenv()


def convert_currency_to_rub(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    try:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
            return float(transaction.get("operationAmount", {}).get("amount"))
    except AttributeError, TypeError, ValueError:
        raise Exception("Неверный формат транзакции")

    apikey = os.getenv("API_KEY")
    if not apikey:
        raise Exception("Не удалось загрузить ключ для подключения к API")

    params = {
        "amount": transaction.get("operationAmount", {}).get("amount"),
        "from": transaction.get("operationAmount", {}).get("currency", {}).get("code"),
        "to": "RUB",
    }
    headers = {"apikey": apikey}

    response = requests.get(URL, params=params, headers=headers)

    if response.status_code != 200:
        raise Exception("Ошибка при обращении к API для конвертации")

    if "result" not in response.json():
        raise ValueError("Неверный формат ответа API")

    return round(float(response.json()["result"]), 2)
