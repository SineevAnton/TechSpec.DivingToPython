# Task 2

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def get_user_fraction() -> str:
    """Мспользуется для получения дроби от пользователя.
    Ввод пользователя проверяется на корректность.
    """

    while True:
        user_input = input("Введите дробь в виде 'a/b', где 'a' и 'b' - числа:\n")
        temp_list = user_input.split('/')
        if len(temp_list) == 2 and temp_list[0].isdigit() and temp_list[1].isdigit():
            user_fraction_numbers = [int(temp_list[0]),int(temp_list[1])]
            break
        else:
            print('Неверный ввод, попробуйте еще раз.')
            continue
    return user_fraction_numbers


def get_fractions_prod(fract_1, fract_2: list) -> list:
    """Функция вычисления произведения двух дробей.

    Parameters
        ----------
        fract_1 : list
            Дробь в виде списка (на 0-й позиции делимое, на 1-й позиции - делитель)
        fract_2 : list
            Дробь в виде списка (на 0-й позиции делимое, на 1-й позиции - делитель)
    """

    fract_prod = [fract_1[0] * fract_2[0],fract_1[1] * fract_2[1]]
    devider = max_devider(fract_prod[0], fract_prod[1])
    fract_prod[0] = int(fract_prod[0] / devider)
    fract_prod[1] = int(fract_prod[1] / devider)
    return fract_prod


def max_devider(num1, num2: int) -> int:
    """Функция для определения наибольшего общего делителя (НОД) двух чисел.

    Parameters
        ----------
        num1, num2: int
            Числа, для которых определяется НОД
    """

    result = 1
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    if max_num % min_num == 0:
        result = min_num
    else:
        for i in range(2, min_num // 2):
            if max_num % i == 0 and min_num % i == 0:
                result = i
    return result


def get_fractions_sum(fract_1, fract_2: list) -> list:
    """Функция вычисления суммы двух дробей.

    Parameters
        ----------
        fract_1 : list
            Дробь в виде списка (на 0-й позиции делимое, на 1-й позиции - делитель)
        fract_2 : list
            Дробь в виде списка (на 0-й позиции делимое, на 1-й позиции - делитель)
    """

    fract_sum = []
    fract_sum.append((fract_1[0] * fract_2[1] + fract_2[0] * fract_1[1]))
    fract_sum.append((fract_1[1] * fract_2[1]))
    devider = max_devider(fract_sum[0], fract_sum[1])
    fract_sum[0] = int(fract_sum[0] / devider)
    fract_sum[1] = int(fract_sum[1] / devider)
    return fract_sum


first_fraction = get_user_fraction()
second_fraction = get_user_fraction()
user_fractions_prod = get_fractions_prod(first_fraction, second_fraction)
user_fractions_sum = get_fractions_sum(first_fraction, second_fraction)

print(f"Произведение дробей {first_fraction[0]}/{first_fraction[1]}"
      f" и {second_fraction[0]}/{second_fraction[1]} равно {user_fractions_prod[0]}/{user_fractions_prod[1]}")

print(f"Сумма дробей {first_fraction[0]}/{first_fraction[1]}"
      f" и {second_fraction[0]}/{second_fraction[1]} равна {user_fractions_sum[0]}/{user_fractions_sum[1]}")

first_check_fraction = Fraction(first_fraction[0], first_fraction[1])
second_check_fraction = Fraction(second_fraction[0], second_fraction[1])
print()
print("Проверка с успользованием модуля Fraction.")
print(f"Произведение равно: {first_check_fraction * second_check_fraction}")
print(f"Сумма равна: {first_check_fraction + second_check_fraction}")
