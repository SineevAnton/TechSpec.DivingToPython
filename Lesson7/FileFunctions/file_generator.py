"""
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""


def generate_files(expansion: str, min_name_length: int = 6, max_name_length: int = 30,
                   min_byte_size: int = 256, max_byte_size: int = 4096, file_count: int = 42) -> None:
    from random import randint
    for _ in range(file_count):
        f_name = ""
        rnd_len = randint(min_name_length, max_name_length)
        for _ in range(rnd_len):
            f_name += chr(randint(97, 122))

        rnd_size = randint(min_byte_size, max_byte_size)
        data = bytes(rnd_size)
        with open(f'files_to_rename/{f_name}.{expansion}', 'ab') as result:
            result.write(data)
