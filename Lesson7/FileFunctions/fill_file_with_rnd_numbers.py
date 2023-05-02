"""
Функция, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число - int, второе - float разделены вертикальной чертой.
Минимальное число: -1000, максимальное: +1000.
Количество строк и имя файла передаются как аргументы функции.
"""

RND_MAX = 1000
RND_MIN = -1000
ROUND_TO = 2


def append_random(str_count: int, f_path: str) -> None:
    """
    Функция, заполняющая файл по заданным условиям.
    :param str_count: количество строк для заполнения
    :param f_path: путь к файлу
    :return: None
    """
    from random import randint, uniform
    with open(f_path, 'a', encoding='utf-8') as f:
        for i in range(str_count):
            f.write(f"{randint(RND_MIN, RND_MAX)}|{round(uniform(RND_MIN, RND_MAX), ROUND_TO)}\n")
