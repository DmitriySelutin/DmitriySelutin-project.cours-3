import json
import os
import re
from typing import Dict, List

from src.logger import logger_setup

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(current_dir, "../logs", "services.log")
logger = logger_setup("services", file_path_log)


def find_person_to_person_transactions(transactions: List[Dict]) -> str:
    """Функция вовзращает транзакции в описании которых есть имя кому или от кого выполнен перевод"""
    try:
        transfer_transactions = []
        search_pattern = re.compile(r"\b[А-ЯЁ][а-яё]*\s[А-ЯЁ]\.")
        for transaction in transactions:
            category = transaction.get("Категория", "")
            description = transaction.get("Описание", "")
            if category == "Переводы" and search_pattern.search(description):
                transfer_transactions.append(transaction)
        logger.info("Выполнен поиск по переводам физлицам")
        return json.dumps(transfer_transactions, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Возникла ошибка {e}")
        logger.error(f"Возникла ошибка {e}")
        return ""
