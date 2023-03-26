# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_dictionary(names, salary, percents: list) -> dict[str, float]:
    """
    Функция генерирует и возвращает словарь, в котором ключ - имя сотрудника, значение - рассчиная величина премии
    :param names: Список имен сотрудников
    :param salary: Список окладов сотрудников
    :param percents: Список назначаемой сотрудникам премии (в процентов)
    :return: Словарь, в котором ключ - имя сотрудника, значение - рассчиная величина премии
    """
    return {
        name: float(sal * perc) for name, sal, perc
        in zip(names, salary, list(map(lambda x: float(x.replace('%', '')) / 100, percents)))
    }


names_list = ["N1", "N2", "N3", "N4"]
salary_list = [1000, 2500, 2000, 3000]
percents_list = ["10.25%", "10.00%", "20.00%", "15.00%"]
result_dict = generate_dictionary(names_list, salary_list, percents_list)
print(result_dict)