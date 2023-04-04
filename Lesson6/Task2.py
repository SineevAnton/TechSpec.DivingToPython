# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Задание 3:
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

def generate_queens_position() -> list[list[int]]:
    """
    Функция случайным образом генерирует расположение 8-ми ферзей на шахматной доске
    :return: Список списков, где каждый вложенный список хранит 2 координаты [строка, колонка] ферзя на доске
    """
    from random import choice
    queen_positions = []
    rows = [0, 1, 2, 3, 4, 5, 6, 7]
    cols = [0, 1, 2, 3, 4, 5, 6, 7]
    while len(queen_positions) < 8:
        # Короткий вариант с количеством сочетаний, равным 16 777 216
        r = choice(rows)
        c = choice(cols)
        queen_positions.append([r, c])
        rows.remove(r)
        cols.remove(c)

        # Длинный вариант с количеством сочетаний 4 426 165 368. НЕ ТРОГАТЬ, это на новый год, там праздники длинные
        # Если время не жалко - расскомментируем, а в импорт выше добавляем randint
        # temp = []
        # for j in range(2):
        #     temp.append(randint(0, 7))
        # if temp not in queen_positions:
        #     queen_positions.append(temp)
    return queen_positions


def print_desk(queens_position: list[list[int]]) -> None:
    """
    Печатает шахматную доску в консоль, расставляя на ней ферзей
    :param queens_position: координаты ферзей для расстановки на доске
    :return: None
    """
    desk = [8*["*"] for _ in range(8)]
    for queen in queens_position:
        desk[queen[0]][queen[1]] = "Q"
    for i in range(8):
        print(desk[i])
    print("________________________________________")


def check_chess_desk(queens_position: list[list[int]]) -> bool:
    """
    Проверяет соответствует ли расстановка ферзей заданному условию:
    ни один ферзь не бьет любого другого ферзя
    :param queens_position: координаты ферзей для расстановки на доске
    :return: True - если ферзи расставлены в соответствии с условием, иначе - False
    """
    is_correct = True
    for i in range(len(queens_position)):
        for j in range(i + 1, len(queens_position)):
            if (queens_position[i][0] == queens_position[j][0] or
                    queens_position[i][1] == queens_position[j][1] or
                    abs(queens_position[i][0] - queens_position[j][0]) ==
                    abs(queens_position[i][1] - queens_position[j][1])):
                is_correct = False
                break
        if not is_correct:
            break
    return is_correct


if __name__ == "__main__":
    generate_count = 1
    while generate_count < 5:
        queens = generate_queens_position()
        if check_chess_desk(queens):
            print(f"Placement option № {generate_count}")
            print(f"Queens coordinates: {queens}\nDesk:")
            print_desk(queens)
            generate_count += 1
