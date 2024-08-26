"""
Модуль formatting содержит функции для форматирования данных о книгах.
"""

def format_book_data(data: dict) -> str:
    """
    Форматирует данные книги в строку.

    :param data: Словарь, содержащий данные книги.
    :return: Строка с форматированной информацией о книге.
    """
    return f"Title: {data['title']}, Author: {data['author']}, Genre: {data['genre']}"

