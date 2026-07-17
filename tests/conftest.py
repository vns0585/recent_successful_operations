import pytest


@pytest.fixture
def processing_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filtered_data_executed() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filtered_data_canceled() -> list:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def processing_data_without_state() -> list:
    return [
        {"id": 41428829, "1": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "1": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "1": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "1": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_data_by_date_descending() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sorted_data_by_date_ascending() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def processing_data_without_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "2": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "2": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "2": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "2": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def processing_data_broken_keys() -> list:
    return [
        {"i": 41428829, "sate": "EXECUTED", "dae": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "dat": "2018-06-30T02:08:58.425572"},
        {"it": 594226727, "stte": "CANCELED", "ate": "2018-09-12T21:27:25.241689"},
        {"d": 615064591, "stat": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def processing_data_list() -> list:
    return [
        [41428829, "EXECUTED", "2019-07-03T18:35:29.512364"],
        [939719570, "EXECUTED", "2018-06-30T02:08:58.425572"],
        [594226727, "CANCELED", "2018-09-12T21:27:25.241689"],
        [615064591, "CANCELED", "2018-10-14T08:21:33.419441"],
    ]
