"""
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
если оно передано. Далее счётчик файлов и расширение.
"""

def rename_files(f_name: str, number_count: int, original_extention: str,
                 final_extention: str, letters_range: list) -> None:
    """
    Функция переименовывает файлы согласно условию выше
    :param f_name: желаемое конечное имя файла
    :param number_count: количество цифр в порядковом номере
    :param original_extention: расширение исходного файла
    :param final_extention: расширение конечного файла
    :param letters_range: диапазон сохраняемого оригинального имени
    :return: None
    """

    import os
    files_list = os.listdir("files_to_rename")
    files_names = [i.split('.')[0] for i in files_list]
    files_count = len(files_names)
    extention_count = 0
    for file in files_list:
        if original_extention in file:
            extention_count += 1
    min_file_name_length = min([len(i) for i in files_names])

    """
    Проверки возможности переименования файлов
    """
    if (10 ** number_count) - 1 < extention_count:
        print(f"Невозможная операция. Количество файлов с расширением '.{original_extention}' "
              f"({extention_count} шт.) больше чем 10^{number_count}-1={extention_count-1}.")
        return
    if letters_range[1] > min_file_name_length:
        print(f"Невозможная операция. Максимальное значение диапазона '{letters_range}' "
              f"должно быть меньше минимальной длины имени файла, равной {min_file_name_length}.")
        return

    file_counter = 0

    for i in range(files_count):
        if original_extention in files_list[i]:
            file_counter += 1
            new_file_name = f"{files_names[i][letters_range[0]:letters_range[1]]}{f_name}{file_counter:0{number_count}}.{final_extention}"
            os.rename(f"files_to_rename/{files_list[i]}", f"files_to_rename/{new_file_name}")
