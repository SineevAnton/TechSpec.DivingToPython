"""
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножте пары чисел. В новый файл сохраните имя и произведение:
- если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
- если результат умножения положительный, сохраните имя прописными буквами и произведение, округленное до целого.
В результирующем файле должно быть столько же строк, сколько и в более длинном файле.
При достижении конца более короткого файла возвращайтесь в его начало.
"""


def task3_solution(numbers_path, names_path, result_path: str) -> None:
    with open(numbers_path, 'r', encoding='utf-8') as f_num, \
            open(names_path, 'r', encoding='utf-8') as f_names, \
            open(result_path, 'w', encoding='utf-8') as f_result:
        len_num = sum(1 for _ in f_num)
        len_names = sum(1 for _ in f_names)

        for _ in range(max(len_num, len_names)):
            name = read_line(f_names)
            number = read_line(f_num)
            split_number = number.split("|")
            prod = int(split_number[0]) * float(split_number[1])
            if prod > 0:
                res = f"{name.upper()} {round(prod)}"
            elif prod < 0:
                res = f"{name.lower()} {round(abs(prod), 2)}"
            f_result.write(res + "\n")


def read_line(f_descr):
    text = f_descr.readline()
    if text == "":
        f_descr.seek(0)
        text = f_descr.readline()

    return text[:-1]


# if __name__ == '__main__':
#     task3_solution("output.txt", "names_output.txt", "task3_result.txt")