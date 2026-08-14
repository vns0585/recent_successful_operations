from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.importers import import_errors, import_from_csv, import_from_excel, prepare_transactions


@patch("src.importers.pd.read_csv")
def test_import_from_csv(mock_pd_read_csv: Mock, transactions_df: pd.DataFrame, transaction_imported: list) -> None:
    mock_pd_read_csv.return_value = transactions_df
    result = import_from_csv("test.csv")
    assert result == transaction_imported
    mock_pd_read_csv.assert_called_once_with("test.csv", delimiter=";")


@patch("src.importers.pd.read_excel")
def test_import_from_excel(mock_pd_read: Mock, transactions_df: pd.DataFrame, transaction_imported: list) -> None:
    mock_pd_read.return_value = transactions_df
    result = import_from_excel("test.xlsx")
    assert result == transaction_imported
    mock_pd_read.assert_called_once_with("test.xlsx")


def test_import_errors_fnf() -> None:
    @import_errors
    def open_file(filename: str) -> list:
        raise FileNotFoundError(filename)
    with pytest.raises(FileNotFoundError, match="Файл не найден."):
        open_file("test.csv")


def test_import_errors_ede() -> None:
    @import_errors
    def open_file(filename: str) -> list:
        raise pd.errors.EmptyDataError(filename)
    result = open_file("test.csv")
    assert result == []


def test_import_errors_exception() -> None:
    @import_errors
    def open_file(filename: str) -> list:
        raise Exception
    with pytest.raises(Exception, match="Ошибка при импорте."):
        open_file("test.csv")


def test_prepare_transactions_without_column(transactions_df: pd.DataFrame, transaction_imported: list) -> None:
    transactions_without_column = transactions_df.copy().drop("id", axis=1)
    with pytest.raises(KeyError, match="Отсутствует колонка с данными."):
        prepare_transactions(transactions_without_column)


def test_prepare_transactions_wrong_data(transactions_df: pd.DataFrame, transaction_imported: list) -> None:
    tr = transactions_df.copy()
    tr["id"] = 88.88
    with pytest.raises(TypeError, match="Некорректный тип данных."):
        prepare_transactions(tr)


def test_prepare_transactions_wrong_dt(transactions_df: pd.DataFrame, transaction_imported: list) -> None:
    tr = transactions_df.copy()
    tr["date"] = "0000-2t-??"
    with pytest.raises(ValueError, match="Некорректные данные."):
        prepare_transactions(tr)
