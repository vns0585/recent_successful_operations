import json
from typing import Any
from unittest.mock import Mock, mock_open, patch

import pytest

from src.utils import load_transactions_from_file


def test_load_transactions_from_file_success(transactions: list) -> None:
    json_transactions = json.dumps(transactions)
    with patch("builtins.open", mock_open(read_data=json_transactions)) as mock_builtins_open:
        result = load_transactions_from_file("test.json")
        assert result == transactions
        mock_builtins_open.assert_called_once_with("test.json", encoding="utf-8")


@pytest.mark.parametrize(
    "data",
    [
        "abracadabra",
        None
    ]
)
def test_load_transactions_from_file_invalid_json(data: Any) -> None:
    with patch("builtins.open", mock_open(read_data=data)) as mock_builtins_open:
        result = load_transactions_from_file("bad.json")
        assert result == []
        mock_builtins_open.assert_called_once_with("bad.json", encoding="utf-8")


def test_load_transactions_from_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError()) as mock_builtins_open:
        result = load_transactions_from_file("missing.json")
        assert result == []
        mock_builtins_open.assert_called_once_with("missing.json", encoding="utf-8")


def test_load_transactions_from_file_error() -> None:
    with patch("builtins.open", side_effect=Exception()) as mock_builtins_open:
        result = load_transactions_from_file("test.json")
        assert result == []
        mock_builtins_open.assert_called_once_with("test.json", encoding="utf-8")


@patch("src.utils.json.load")
def test_load_transactions_from_file_exception(mock_json_load: Mock, transactions: list) -> None:
    mock_json_load.return_value = "abracadabra"
    json_transactions = json.dumps(transactions)
    with patch("builtins.open", mock_open(read_data=json_transactions)) as mock_builtins_open:
        result = load_transactions_from_file("test.json")
        assert result == []
        mock_builtins_open.assert_called_once_with("test.json", encoding="utf-8")
        mock_json_load.assert_called_once()
