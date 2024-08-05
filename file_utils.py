"""
file_utils.py

Этот модуль содержит функции для работы с файлами, такие как чтение
содержимого текстового файла и выбор случайной строки.
"""

import random

def read_file(file_path):
    """
    Читает и возвращает содержимое файла по указанному пути.

    :param file_path: Путь к файлу.
    :return: Строка с содержимым файла или None, если файл не найден.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")



