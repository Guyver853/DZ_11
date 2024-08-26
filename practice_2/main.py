# main.py

# Импортирование ключевых компонентов
from data_processing import DataProcessor, data_utils # Инициализация пакета data_processing
from data_processing.preprocessing.data_cleaning import clean_data # Инициализация подпакета preprocessing
from data_processing.postprocessing.report_generation import generate_report # Инициализация подпакета postprocessing

data = "выборочные данные"

# Создание экземпляра обработчика данных
processor = DataProcessor() # DataProcessor инициализирован
processor.process(data) # Обработка данных: выборочные данные

# Использование вспомогательных функций
data_utils() # Функция полезности для data processing

# Применение функций из подпакетов
clean_data(data) # Данные по очистке: выборочные данные
generate_report(data) # Формирование отчета по данным: выборочные данные


"""
Объяснение

Инициализация пакета и подпакетов: Файлы __init__.py в корневом пакете и подпакетах обеспечивают инициализацию и настройку при первом импорте. 
Например, при импорте data_processing будет выведено сообщение "Инициализация пакета data_processing".

Управление экспортом: В каждом __init__.py можно определить переменную __all__, чтобы указать, какие модули доступны при использовании from package import *.

Вложенные пакеты: Подпакеты preprocessing и postprocessing имеют свои собственные файлы __init__.py, что позволяет организовывать модули в логическую иерархию.
"""