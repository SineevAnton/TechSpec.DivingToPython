# Task 3

# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
import time
lower_limit = 0
upper_limit = 1000
gen_number = randint(lower_limit, upper_limit)


def guess_the_number(number, low_limit, up_limit: int):
    """Угадывает переданное число используя бинарный 'поиск'

        Parameters
        ----------
        number : int
            Угадываемое число
        low_limit : int
            Нижняя граница диапазона, в котором было сгенерированно число
        up_limit : int
            Верхняя граница диапазона, в котором было сгенерированно число
    """

    try_counts = 0
    while True:
        time.sleep(0.5)
        try_num = (up_limit + low_limit) // 2
        if number == try_num:
            print(f"\nВы угадали!\n Ваше число {try_num} равно загаданному {number}\n"
                  f" Число попыток равно: {try_counts}.")
            break
        else:
            # ниже оставил в выводе сгенерированное число и как меняются диапазоны после каждого шага
            # сделано для наглядности
            if try_num > number:
                print(f"Ваше число {try_num} больше загаданного {number}. Новый диапазон: ({low_limit},{up_limit})")
                up_limit = sum(divmod(low_limit + up_limit,2))
                try_counts += 1
            else:
                print(f"Ваше число {try_num} меньше загаданного {number}. Новый диапазон: ({low_limit},{up_limit})")
                low_limit = (low_limit + up_limit) // 2
                try_counts += 1


guess_the_number(gen_number, lower_limit, upper_limit)