# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def check_hash(obj):
    """
    Функция проверки является ли переданный объект хэшируемым
    :param obj: проверяемый объект
    :return: True, если переданный объект хэшируемый, иначе - False
    """

    try:
        hash(obj)
        return True
    except Exception as ex:
        return False


def get_dict_from_kwargs(**kwargs) -> dict:
    """
    Функция, принимающая ключевые аргументы, и возвращающая словарь, где
    ключ - значение аргумента, а значение - имя аргумента
    :param kwargs: передаваемые аргументы
    :return: result_dict - новый сформированный словарь
    """

    result_dict = {}
    for key, value in kwargs.items():
        if check_hash(value):
            result_dict[value] = key
        else:
            result_dict[str(value)] = key
    return result_dict


test_dict = get_dict_from_kwargs(name="Name", age=25, sex="M", data=[1, 2, 33])
print(test_dict)
