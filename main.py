"""
Главный модуль для взаимодействия с библиотекой.

Создает экземпляр класса Library, добавляет книги, ищет и удаляет их
и генерирует отчеты о содержимом библиотеки.
"""

from library_manager import Library, generate_report

def main():
    # Создание экземпляра библиотеки
    my_library = Library()

    # Добавление книг
    my_library.add_book("Мастер и Маргарита", "Михаил Булгаков", "Фэнтези")
    my_library.add_book("Дом, в котором…", "Мариам Петросян", "Магический реализм")

    # Просмотр всех книг
    print("Книги в библиотеке:")
    print(generate_report(my_library))

    # Поиск книги
    print("\nПоиск книги 'Мастер и Маргарита':")
    found_books = my_library.find_book(title="Мастер и Маргарита")

    # Генерация отчета о найденных книгах
    if found_books:
        # Создаем новый экземпляр библиотеки для найденных книг
        found_library = Library()
        for book in found_books:
            found_library.add_book(book['title'], book['author'], book['genre'])
        print(generate_report(found_library))  # Выводим найденные книги
    else:
        print("Книга не найдена.")

    # Удаление книги
    my_library.remove_book("Мастер и Маргарита")

    # Проверка оставшихся книг
    print("\nКниги в библиотеке после удаления:")
    print(generate_report(my_library))

if __name__ == "__main__":
    main()