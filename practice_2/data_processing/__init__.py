# data_processing/__init__.py

# Выполняется при первом импорте пакета
print("Инициализация пакета data_processing")

# Определение списка экспортируемых модулей
__all__ = ['core', 'utils', 'preprocessing', 'postprocessing']

# Импортирование ключевых функций и классов для удобства
from .core import DataProcessor
from .utils import data_utils
