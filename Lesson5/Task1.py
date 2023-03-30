# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_path_values(absolute_path: str) -> tuple:
    """
    Функция принимает абсолютный путь к файлу и фозвращает кортеж,
    содержащий путь, имя и расширение файла
    :param absolute_path: строка - абсулютный путь к файлу
    :return: кортеж из пути, имени и расширения файла
    """
    values = absolute_path.split('\\')
    result = ('\\'.join(values[:-1]), values[-1].split('.')[0], values[-1].split('.')[1])
    return result


path = 'C:\Thecode\Media\статья.txt'
path_values = get_path_values(path)
values_names = ['Путь', 'Имя файла', 'Расширение файла']
for i in range(3):
    print(f"{values_names[i]}: {path_values[i]}")
