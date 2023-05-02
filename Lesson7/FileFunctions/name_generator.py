"""
Написать функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохранять в файл.
"""


def generate_name(f_path: str, names_count: int) -> None:
    from random import randint, choice
    letters = 'aeiouy'

    with open(f_path, 'w', encoding='utf-8') as f:
        for _ in range(names_count):
            name = ''
            for i in range(randint(4, 7)):
                if i == 0:
                    name += chr(randint(97, 122)).upper()
                elif i % 2 == 0:
                    name += chr(randint(97, 122))
                else:
                    name += choice(letters)
            f.write(f"{name}\n")
