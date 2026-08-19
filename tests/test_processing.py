import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state_executed(processing_data: list, filtered_data_executed: list) -> None:
    assert filter_by_state(processing_data, "EXECUTED") == filtered_data_executed


def test_filter_by_state_canceled(processing_data: list, filtered_data_canceled: list) -> None:
    assert filter_by_state(processing_data, "CANCELED") == filtered_data_canceled


def test_filter_by_state_wrong_type(processing_data_list: list) -> None:
    with pytest.raises(AttributeError, match="В списке данные неверного типа. Ожидаются словари."):
        filter_by_state(processing_data_list, "EXECUTED")


def test_sort_by_date_descending(processing_data: list, sorted_data_by_date_descending: list) -> None:
    assert sort_by_date(processing_data, True) == sorted_data_by_date_descending


def test_sort_by_date_ascending(processing_data: list, sorted_data_by_date_ascending: list) -> None:
    assert sort_by_date(processing_data, False) == sorted_data_by_date_ascending


def test_sort_by_date_wrong_type(processing_data_list: list) -> None:
    with pytest.raises(AttributeError, match="В списке данные неверного типа. Ожидаются словари."):
        sort_by_date(processing_data_list)


def test_process_bank_search(transactions: list[dict], filtered_data_bank_search: list) -> None:
    assert process_bank_search(transactions, "счет") == filtered_data_bank_search


def test_process_bank_search_none(transactions: list[dict]) -> None:
    assert process_bank_search(transactions, None) == []


def test_process_bank_operations(transactions: list[dict], filtered_data_bank_operations: dict) -> None:
    assert process_bank_operations(transactions, ["Перевод организации", "Перевод с карты на карту"]) \
           == filtered_data_bank_operations
