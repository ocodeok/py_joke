"""
config.py

Этот модуль содержит конфигурационные параметры и пути, используемые в проекте.
Определяет базовую директорию и путь к файлу `taunting_players.txt`.
"""

from pathlib import Path

# Define the base directory as the current working directory.
BASE_DIR = Path.cwd()

# Define the base name of file
JOKES_FILE = 'jokes.txt'

# Full path to file
PATH_TO_JOKES = BASE_DIR / JOKES_FILE
