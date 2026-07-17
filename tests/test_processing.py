import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(processing_data: list, filtered_data_executed: list) -> None:
    assert filter_by_state(processing_data, "EXECUTED") == filtered_data_executed


def test_filter_by_state_canceled(processing_data: list, filtered_data_canceled: list) -> None:
    assert filter_by_state(processing_data, "CANCELED") == filtered_data_canceled


def test_filter_by_state_without_state(processing_data_without_state: list) -> None:
    with pytest.raises(KeyError) as e:
        filter_by_state(processing_data_without_state, "EXECUTED")
    assert e.value.args[0] == "В переданных словарях отсутствует ключ 'state'."


def test_filter_by_state_broken_keys(processing_data_broken_keys: list) -> None:
    with pytest.raises(KeyError) as e:
        filter_by_state(processing_data_broken_keys, "EXECUTED")
    assert e.value.args[0] == "В переданных словарях отсутствует ключ 'state'."


def test_filter_by_state_wrong_type(processing_data_list: list) -> None:
    with pytest.raises(TypeError) as e:
        filter_by_state(processing_data_list, "EXECUTED")
    assert e.value.args[0] == "В списке данные неверного типа. Ожидаются словари."


def test_sort_by_date_descending(processing_data: list, sorted_data_by_date_descending: list) -> None:
    assert sort_by_date(processing_data, True) == sorted_data_by_date_descending


def test_sort_by_date_ascending(processing_data: list, sorted_data_by_date_ascending: list) -> None:
    assert sort_by_date(processing_data, False) == sorted_data_by_date_ascending


def test_sort_by_date_without_date(processing_data_without_date: list) -> None:
    with pytest.raises(KeyError) as e:
        sort_by_date(processing_data_without_date)
    assert e.value.args[0] == "В переданных словарях отсутствует ключ 'date'."


def test_sort_by_date_broken_keys(processing_data_broken_keys: list) -> None:
    with pytest.raises(KeyError) as e:
        sort_by_date(processing_data_broken_keys)
    assert e.value.args[0] == "В переданных словарях отсутствует ключ 'date'."


def test_sort_by_date_wrong_type(processing_data_list: list) -> None:
    with pytest.raises(TypeError) as e:
        sort_by_date(processing_data_list)
    assert e.value.args[0] == "В списке данные неверного типа. Ожидаются словари."
