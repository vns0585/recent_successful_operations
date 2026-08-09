import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import convert_currency_to_rub

load_dotenv()
apikey = os.getenv("API_KEY")
transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}


def test_convert_currency_to_rub_rub(transactions_rub: list) -> None:
    result = convert_currency_to_rub(transactions_rub[0])
    assert result == float(transactions_rub[0]["operationAmount"]["amount"])


@patch("src.external_api.requests.get")
def test_convert_currency_to_rub_usd(mocked_get: Mock) -> None:
    mocked_get.return_value.json.return_value = {"result": "82.55"}
    mocked_get.return_value.status_code = 200
    result = convert_currency_to_rub(transaction)
    assert result == 82.55
    mocked_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"amount": "1", "from": "USD", "to": "RUB"},
        headers={"apikey": apikey},
    )


@patch("src.external_api.requests.get")
def test_convert_currency_to_rub_usd_bad_status(mocked_get: Mock) -> None:
    mocked_get.return_value.status_code = 404
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    with pytest.raises(Exception, match="Ошибка при обращении к API для конвертации"):
        convert_currency_to_rub(transaction)


@patch("src.external_api.requests.get")
def test_convert_currency_to_rub_usd_bad_response(mocked_get: Mock) -> None:
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    with pytest.raises(ValueError, match="Неверный формат ответа API"):
        convert_currency_to_rub(transaction)


def test_convert_currency_to_rub_usd_bad_transaction() -> None:
    transaction = {"operationAmount": "kjkj"}
    with pytest.raises(Exception, match="Неверный формат транзакции"):
        convert_currency_to_rub(transaction)


@patch("src.external_api.os.getenv")
def test_convert_currency_to_rub_usd_bad_environment(mock_os_getenv: Mock) -> None:
    mock_os_getenv.return_value = None
    with pytest.raises(Exception, match="Не удалось загрузить ключ для подключения к API"):
        convert_currency_to_rub(transaction)
    mock_os_getenv.assert_called_once_with("API_KEY")
