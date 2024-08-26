"""
Модуль data_validation содержит функции для проверки данных книги.
"""

def validate_book_data(data: dict) -> bool:
    """
    Проверяет, содержит ли данные книги все необходимые поля.

    :param data: Словарь, содержащий данные книги.
    :return: True, если все поля присутствуют, иначе False.
    """
    required_fields = ['title', 'author', 'genre']
    return all(field in data for field in required_fields)

