"""
Функция для очистки содержимого файла
"""


def clear_file(f_path: str) -> None:
    """
    Функция для очистки файла
    :param f_path: футь к файлу
    :return: None
    """
    open(f_path, 'w').close()