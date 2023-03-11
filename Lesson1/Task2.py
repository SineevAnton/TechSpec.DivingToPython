# Task_2

# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def get_user_number() -> int:
    """Мспользуется для получения числа от пользователя, с проверкой корректности ввода
        согласно поставленным условиям.

    """

    try:
        number = int(input("Введите целое положительное число меньше 100 000.\n"))
        if number < 0 or number > 100_000:
            raise Exception
        else:
            return number
    except:
        print('Ошибка ввода')


def is_number_simple(number: int) -> bool:
    """Мспользуется для проверки являестя ли число простым или составным

        Parameters
        ----------
        number : int
            Проверяемое число
    """

    is_simple = True
    delimiters = 0
    numbers = [i for i in range(1, number + 1)]
    for num in numbers:
        if number % num == 0:
            delimiters += 1
    if delimiters > 2:
        is_simple = False
    return is_simple


user_number = get_user_number()
if is_number_simple(user_number):
    print(f"Число {user_number} является простым.")
else:
    print(f"Число {user_number} является составным.")