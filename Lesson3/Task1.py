# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def generate_list() -> list:
    """
    Функция генерации списка целых чисел.
    Логика организована так, чтобы с большой долей вероятности в списке оказались повторяющиеся элементы.
    :return list: список целых чисел
    """

    from random import randint

    result_list = []
    for _ in range(10):
        result_list.append(randint(1, 10))

    return result_list

def check_duplicate(input_list: list) -> list:
    """
    Функция возвращает список элементов, которые дублируются в передаваемом списке.
    :param input_list: список для проверки дублирующихся элементов
    :return result_list: список элементов элементов, имеющих дубликаты в исходном списке
    """

    result_list = []
    unique_elements = set(input_list)
    for element in unique_elements:
        if input_list.count(element) > 1:
            result_list.append(element)

    return result_list


test_list = generate_list()
print(f"Исходный массив:\n{test_list}")
duplicated_elements = check_duplicate(test_list)
print(f"Дублирующиеся элементы:\n{duplicated_elements}")