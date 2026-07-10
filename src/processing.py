def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Возвращает новый список, содержащий только те словари, у которых ключ state соответствует."""
    return [item for item in list_of_dict if item["state"] == state]


def sort_by_date(list_of_dict: list, ascending: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате (ключ date), в указанном порядке."""
    return sorted(list_of_dict, key=lambda item: item["date"], reverse=ascending)


if __name__ == "__main__":
    # Проверка работы функции filter_by_state
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )

    # Проверка работы функции sort_by_date
    print()
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
    )
