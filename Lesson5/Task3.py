# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def generate_fibonacci(numbers_count: int) -> list[int]:
    """
    Функция-генератор (используется ключевое слово yield) генерирует числа Фибонначи
    в количестве, равном 'numbers_count'
    :param numbers_count: количество чисел для генерации
    :return: None
    """
    prev, current = 0, 1
    for _ in range(numbers_count):
        yield prev
        current = prev + current
        prev = current - prev


print(list(generate_fibonacci(10)))