from typing import Any

from src.config import (
    api_key_currency,
    api_key_stocks,
    input_data_reports,
    input_date_str,
    transactions,
    transactions_reports,
    user_settings,
)
from src.reports import spending_by_weekday
from src.services import find_person_to_person_transactions
from src.views import web_page_home


def main() -> Any:
    """Функция для запуска всего проекта"""
    # Главная страница
    print("\nГЛАВНАЯ\n")
    print(web_page_home(input_date_str, user_settings, api_key_currency, api_key_stocks))

    # Cтраница сервиса
    print("\nСЕРВИСЫ\n")
    find_person_to_person_transactions_result = find_person_to_person_transactions(transactions)
    print(find_person_to_person_transactions_result)

    # Страница отчета
    print("\nОТЧЕТЫ\n")
    spending_by_weekday_result = spending_by_weekday(transactions_reports, input_data_reports)
    print(spending_by_weekday_result)


if __name__ == "__main__":
    main()
