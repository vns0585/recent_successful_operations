import json
import logging
import os

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions_from_file(json_file: str = "data/operations.json") -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Открытие файла с транзакциями {json_file}")
    try:
        with open(json_file, encoding="utf-8") as file:
            logger.debug("Загрузка данных из файла.")
            data = json.load(file)
            logger.debug("Данные успешно загружены.")
            if not isinstance(data, list):
                logger.error(f"Содержимое файла не соответствует формату json. Полученный формат: {type(data)}")
                return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {type(e).__name__}")
        return []
    logger.info("Транзакции успешно загружены.")
    return data
