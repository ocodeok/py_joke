import random

import keyboard
import pyperclip

from file_utils import read_file
from config import PATH_TO_JOKES


def get_jokes(path_to_file: str) -> list[str]:
    """Считывает содержимое файла и возвращает список строк (шуток)."""

    content = read_file(path_to_file)
    if not content:
        return []
    return content.split("\n")


def on_hotkey(jokes):
    """Обработчик нажатия горячей клавиши."""
    joke = random.choice(jokes)

    pyperclip.copy(joke)

    # Получение строки из буфера обмена
    clipboard_content = pyperclip.paste()
    print(f"Содержимое буфера обмена: {clipboard_content}")


def main():
    jokes = get_jokes(PATH_TO_JOKES)

    # Проверяем, не пустой ли список шуток
    if not jokes:
        print("Файл с шутками пуст или не удалось прочитать содержимое.")
        return

    hotkey = 'ctrl+v'

    try:
        keyboard.add_hotkey(hotkey, lambda: on_hotkey(jokes))
        print(f"Горячая клавиша для вставки шутки: {hotkey}")
        print("Нажмите 'esc' для выхода.")

        keyboard.wait('esc')
    except KeyboardInterrupt:
        print("Программа завершена.")


if __name__ == "__main__":
    main()
