import json


def load_transactions_from_file(json_file: str = "data/operations.json") -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(json_file, encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
    except Exception as e:
        print(e)
        return []
    return data
