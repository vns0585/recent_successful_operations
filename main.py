from src import generators, importers, processing, utils, widget


def main() -> None:
    """Предоставляет пользовательский интерфейс и связывает функциональности между собой"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    user_file_format = None
    while True:
        try:
            user_file_format = int(input(
                "Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла\n"
            ))
            if user_file_format not in (1, 2, 3):
                raise ValueError
        except ValueError:
            print("Введите номер одного из предложенных вариантов.")
            continue
        else:
            break
    if user_file_format == 1:
        print("Для обработки выбран JSON-файл.\n")
        transactions = utils.load_transactions_from_file()
    elif user_file_format == 2:
        print("Для обработки выбран CSV-файл.\n")
        transactions = importers.import_from_csv()
    elif user_file_format == 3:
        print("Для обработки выбран XLSX-файл.\n")
        transactions = importers.import_from_excel()

    while True:
        user_transaction_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if user_transaction_status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
            print(f"Статус операции \"{user_transaction_status}\" недоступен.")
            continue
        else:
            break
    transactions = processing.filter_by_state(transactions, user_transaction_status.upper())
    print(f"Операции отфильтрованы по статусу \"{user_transaction_status.upper()}\"\n")

    user_sort_by_date = ""
    while user_sort_by_date.upper() not in ("ДА", "НЕТ"):
        user_sort_by_date = input("Отсортировать операции по дате? Да/Нет\n")

    if user_sort_by_date.upper() == "ДА":
        user_sort_asc_dsc = ""
        while user_sort_asc_dsc.lower() not in ("по возрастанию", "по убыванию"):
            user_sort_asc_dsc = input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")
        if user_sort_asc_dsc.lower() == "по возрастанию":
            transactions = processing.sort_by_date(transactions, False)
        else:
            transactions = processing.sort_by_date(transactions)

    user_rub_only = ""
    while user_rub_only.upper() not in ("ДА", "НЕТ"):
        user_rub_only = input("Выводить только рублевые транзакции? Да/Нет\n")

    if user_rub_only.upper() == "ДА":
        transactions = list(generators.filter_by_currency(transactions, "RUB"))

    user_filter_by_word = ""
    while user_filter_by_word.upper() not in ("ДА", "НЕТ"):
        user_filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

    if user_filter_by_word.upper() == "ДА":
        user_filter_word = input("Введите слово для фильтрации.\n")
        transactions = processing.process_bank_search(transactions, user_filter_word)

    if len(transactions) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")
    try:
        if transactions:
            for transaction in transactions:
                print(f"{widget.get_date(transaction.get("date"))} {transaction.get("description")}\n"
                      f"{widget.mask_account_card(transaction.get("from"))} -> "
                      f"{widget.mask_account_card(transaction.get("to"))}\n"
                      f"Сумма: {transaction.get("operationAmount", {}).get("amount")} "
                      f"{transaction.get("operationAmount", {}).get("currency", {}).get("name")}\n")
    except Exception:
        print(transaction)


if __name__ == "__main__":
    main()
