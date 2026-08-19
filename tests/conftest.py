import pandas as pd
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
def processing_data_list() -> list:
    return [
        [41428829, "EXECUTED", "2019-07-03T18:35:29.512364"],
        [939719570, "EXECUTED", "2018-06-30T02:08:58.425572"],
        [594226727, "CANCELED", "2018-09-12T21:27:25.241689"],
        [615064591, "CANCELED", "2018-10-14T08:21:33.419441"],
    ]


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_usd() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def transactions_rub() -> list:
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_description() -> list[str]:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def transactions_df() -> pd.DataFrame:
    data = {
        'id':
            {
                0: '650703', 1: '3598919', 2: '593027', 3: '366176', 4: '5380041'
            },
        'state':
            {
                0: 'EXECUTED', 1: 'EXECUTED', 2: 'CANCELED', 3: 'EXECUTED', 4: 'CANCELED'
            },
        'date':
            {
                0: '2023-09-05T11:30:32Z', 1: '2020-12-06T23:00:58Z', 2: '2023-07-22T05:02:01Z',
                3: '2020-08-02T09:35:18Z', 4: '2021-02-01T11:54:58Z'
            },
        'amount':
            {
                0: '16210', 1: '29740', 2: '30368', 3: '29482', 4: '23789'
            },
        'currency_name':
            {
                0: 'Sol', 1: 'Peso', 2: 'Shilling', 3: 'Rupiah', 4: 'Peso'
            },
        'currency_code':
            {
                0: 'PEN', 1: 'COP', 2: 'TZS', 3: 'IDR', 4: 'UYU'
            },
        'from':
            {
                0: 'Счет 58803664561298323391', 1: 'Discover 3172601889670065', 2: 'Visa 1959232722494097',
                3: 'Discover 0325955596714937', 4: ''
            },
        'to':
            {
                0: 'Счет 39745660563456619397', 1: 'Discover 0720428384694643', 2: 'Visa 6804119550473710',
                3: 'Visa 3820488829287420', 4: 'Счет 23294994494356835683'
            },
        'description':
            {
                0: 'Перевод организации', 1: 'Перевод с карты на карту', 2: 'Перевод с карты на карту',
                3: 'Перевод с карты на карту', 4: 'Открытие вклада'
            }
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def transaction_imported() -> list:
    return [
        {
            'id': 650703,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32.000000',
            'operationAmount':
                {
                    'amount': '16210',
                    'currency':
                        {
                            'name': 'Sol',
                            'code': 'PEN'
                        }
                },
            'description': 'Перевод организации',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397'
        },
        {
            'id': 3598919,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58.000000',
            'operationAmount':
                {
                    'amount': '29740',
                    'currency':
                        {
                            'name': 'Peso',
                            'code': 'COP'
                        }
                },
            'description': 'Перевод с карты на карту',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643'
        },
        {
            'id': 593027,
            'state': 'CANCELED',
            'date': '2023-07-22T05:02:01.000000',
            'operationAmount':
                {
                    'amount': '30368',
                    'currency':
                        {
                            'name': 'Shilling',
                            'code': 'TZS'
                        }
                },
            'description': 'Перевод с карты на карту',
            'from': 'Visa 1959232722494097',
            'to': 'Visa 6804119550473710'
        },
        {
            'id': 366176,
            'state': 'EXECUTED',
            'date': '2020-08-02T09:35:18.000000',
            'operationAmount':
                {
                    'amount': '29482',
                    'currency':
                        {
                            'name': 'Rupiah',
                            'code': 'IDR'
                        }
                },
            'description': 'Перевод с карты на карту',
            'from': 'Discover 0325955596714937',
            'to': 'Visa 3820488829287420'},
        {
            'id': 5380041,
            'state': 'CANCELED',
            'date': '2021-02-01T11:54:58.000000',
            'operationAmount':
                {
                    'amount': '23789',
                    'currency':
                        {
                            'name': 'Peso',
                            'code': 'UYU'
                        }
                },
            'description': 'Открытие вклада',
            'from': '',
            'to': 'Счет 23294994494356835683'
        }
    ]


@pytest.fixture
def filtered_data_bank_search() -> list:
    return [
        {
            'id': 142264268,
            'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount':
                {
                    'amount': '79114.93',
                    'currency':
                        {
                            'name': 'USD',
                            'code': 'USD'
                        }
                },
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'
        },
        {
            'id': 873106923,
            'state': 'EXECUTED',
            'date': '2019-03-23T01:09:46.296404',
            'operationAmount':
                {
                    'amount': '43318.34',
                    'currency':
                        {
                            'name': 'руб.',
                            'code': 'RUB'
                        }
                },
            'description': 'Перевод со счета на счет',
            'from': 'Счет 44812258784861134719',
            'to': 'Счет 74489636417521191160'
        }
    ]


@pytest.fixture
def filtered_data_bank_operations() -> dict:
    return {
        'Перевод организации': 2,
        'Перевод с карты на карту': 1
    }
