"""
Модуль catalog содержит класс Library.

Класс Library управляет коллекцией книг и предоставляет функции для добавления,
удаления, поиска и просмотра книг.
"""

class Library:
    def __init__(self):
        """Инициализирует пустую коллекцию книг."""
        self.books = []

    def add_book(self, title, author, genre):
        """
        Добавляет книгу в коллекцию.

        :param title: Название книги.
        :param author: Автор книги.
        :param genre: Жанр книги.
        """
        book = {'title': title, 'author': author, 'genre': genre}
        self.books.append(book)

    def remove_book(self, title):
        """
        Удаляет книгу из коллекции по названию.

        :param title: Название книги для удаления.
        """
        self.books = [book for book in self.books if book['title'] != title]

    def find_book(self, title=None, author=None, genre=None):
        """
        Ищет книги по параметрам.

        :param title: Название книги для поиска.
        :param author: Автор книги для поиска.
        :param genre: Жанр книги для поиска.
        :return: Список найденных книг.
        """
        results = self.books
        if title:
            results = [book for book in results if book['title'] == title]
        if author:
            results = [book for book in results if book['author'] == author]
        if genre:
            results = [book for book in results if book['genre'] == genre]
        return results

    def view_books(self):
        """
        Возвращает список всех книг в библиотеке.

        :return: Список книг.
        """
        return self.books
