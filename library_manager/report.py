"""
Модуль report предоставляет функции для генерации отчетов о книгах.
"""

def generate_report(library):
    """
    Генерирует отчет о книгах в библиотеке.

    :param library: Экземпляр класса Library.
    :return: Строка с отчетом о книгах.
    """
    report_lines = [f"Название: {book['title']}, Автор: {book['author']}, Жанр: {book['genre']}"
                    for book in library.view_books()]
    return "\n".join(report_lines)
