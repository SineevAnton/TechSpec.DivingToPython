# Task 1

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def get_user_number() -> int:
    """Мспользуется для получения числа от пользователя.

    """

    while True:
        user_input = input("Введите целое число:\n")
        if user_input.isdigit():
            number = int(user_input)
            break
        else:
            print('Неверный ввод, попробуйте еще раз.')
            continue
    return number


def convert_to_hex(number: int) -> str:
    """Преобразовывает переданное десятичное число в его шестнадцатиричное представление.
    Алгоритм преобразования:
    https://sistemy-schisleniya.ru/perevody/iz-desyatichnoj-v-shestnadtsaterichnuyu?ysclid=lf4bw11ug5750944005

    Parameters
        ----------
        number : int
            Переводимое число

    """

    hex_dictionary = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    hex_num = ''

    while number != 0:
        div_nod_pair = divmod(number, 16)
        hex_num += hex_dictionary[div_nod_pair[1]]
        number = div_nod_pair[0]

    return hex_num[::-1]


test_number = get_user_number()
print(f"Число {test_number} в 16-ти ричной системе (используя свою функцию): {convert_to_hex(test_number)}\n"
      f"Проверка с помощью встроенной функции hex(): {hex(test_number)[2:]}")
# При использовании hex() срез [2:] взят, чтобы избавиться от префикса 0x
