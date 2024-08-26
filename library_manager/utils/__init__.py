"""
Инициализирует пакет utils.

Импортирует функции для валидации данных и форматирования выходных данных:
- validate_book_data: Проверяет правильность данных книги.
- format_book_data: Форматирует строку для отчетов.
"""
from .data_validation import validate_book_data
from .formatting import format_book_data

__all__ = ['validate_book_data', 'format_book_data']

