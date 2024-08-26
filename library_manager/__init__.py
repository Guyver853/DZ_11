"""
Инициализирует пакет library_manager.

Импортирует классы и функции для работы с библиотекой:
- Library: Класс для управления коллекцией книг.
- generate_report: Функция для генерации отчета о книгах.
"""
from .catalog import Library
from .report import generate_report

__all__ = ['Library', 'generate_report']


