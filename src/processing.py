def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Возвращает новый список, содержащий только те словари, у которых ключ state соответствует."""
    try:
        return [item for item in list_of_dict if item["state"] == state]
    except KeyError:
        raise KeyError("В переданных словарях отсутствует ключ 'state'.")
    except TypeError:
        raise TypeError("В списке данные неверного типа. Ожидаются словари.")


def sort_by_date(list_of_dict: list, descending: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате (ключ date), в указанном порядке."""
    try:
        return sorted(list_of_dict, key=lambda item: item["date"], reverse=descending)
    except KeyError:
        raise KeyError("В переданных словарях отсутствует ключ 'date'.")
    except TypeError:
        raise TypeError("В списке данные неверного типа. Ожидаются словари.")
