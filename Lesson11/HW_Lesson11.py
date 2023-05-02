# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    """
    Класс Matrix.
    Функции:
    - создание матриц
    - вывод матриц
    - проверка размерности матриц на равенство
    - сравнение матриц
    - сложение матриц
    - перемножение матриц
    Часть операция возможна только при определенной размерности обеих матриц. В случае ошибок выводятся пояснения.
    """

    def __init__(self, my_list: list[list]):
        self.my_list = my_list
        self.rows_count = len(my_list)
        self.cols_count = len(my_list[0])

    def __str__(self):
        print('\n'.join(map(str, self.my_list)))

    def __checkDimentions__(self, second_mat):
        """
        Функция проверки размерности матриц на одинаковость
        :param second_mat: матрица, с которой сравнивается текущий экземпляр класса
        :return: True, если размерности матриц равны, иначе False
        """
        return self.rows_count == second_mat.rows_count and self.cols_count == second_mat.cols_count

    def __compareMatrix__(self, second_mat):
        """
        Поэлементное сравнение матриц. Возможно только для матриц одного размера.
        :param second_mat: матрица, с которой сравнивается текущий экземпляр класса
        :return: True - если матрицы равны, False - если не равны, текстовое описание ошибки в случае отличающихся
        размерностей матриц
        """
        flag = True
        if self.__checkDimentions__(second_mat):
            for i in range(self.rows_count):
                for j in range(self.cols_count):
                    if self.my_list[i][j] != second_mat.my_list[i][j]:
                        flag = False
                        break
            return flag
        else:
            return 'Ошибка. Сравнение невозможно. Размерности матриц не совпадают!'

    def __add__(self, second_mat):
        """
        Поэлементное сложение матриц. Возможно только для матриц одного размера. Исходные матрицы не изменяются
        :param second_mat: матрица, которая прибавляется к текущий экземпляру класса
        :return: Экземпляр класса Matrix, равный сумме двух матриц
        """
        if self.__checkDimentions__(second_mat):
            result = Matrix(second_mat.my_list)
            for i in range(self.rows_count):
                for j in range(self.cols_count):
                    result.my_list[i][j] = self.my_list[i][j] + second_mat.my_list[i][j]
            return result
        else:
            return 'Ошибка. Сложение невозможно. Размерности матриц не совпадают!'

    def __matMult__(self, second_mat):
        """
        Матричное произведение. Возможно только если размерности матриц имеют вид MxN и NxK. Исходные матрицы не
        изменяются
        :param second_mat: матрица, которая прибавляется к текущий экземпляру класса
        :return: Экземпляр класса Matrix, равный произведению двух матриц
        """
        if self.cols_count == second_mat.rows_count:
            zip_b = list(zip(*second_mat.my_list))
            return Matrix([[sum(el_a * el_b for el_a, el_b in zip(row_a, col_b))
                     for col_b in zip_b] for row_a in self.my_list])
        else:
            return 'Умножение невозможно. Неверная размерность матриц.'


"""
Далее идет демонстрация работы класса.
Создание матриц, вывод в консоль.
Сложение и умножение
"""

a = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
b = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print('Исходная матрица a:')
a.__str__()
print()
print('Исходная матрица b:')
b.__str__()
print()
print('Сумма двух матриц:')
a.__add__(b).__str__()

print()
a = Matrix([[-1, 1, 2], [-1, 2, 1]])
b = Matrix([[-2, 1, 3], [-2, 2, 3]])
print('Пробуем перемножить матрицы:')
a.__str__()
print()
b.__str__()
a.__matMult__(b).__str__()

print()
a = Matrix([[-1, 1], [-1, 2]])
b = Matrix([[-2, 1, 3], [-2, 2, 3]])
print('Пробуем перемножить матрицы:')
a.__str__()
print()
b.__str__()
print('Результат:')
a.__matMult__(b).__str__()
print(f'Сравним, равны ли перемножаемые матрицы: {a.__compareMatrix__(b)}')

print()
print('Еще о сравнении матриц:')
a = Matrix([[-1, 1], [-1, 2]])
b = Matrix([[-1, 1], [-1, 2]])
a.__str__()
print()
b.__str__()
print('Результат:')
print(f'Матрицы равны: {a.__compareMatrix__(b)}')

print()
a = Matrix([[-1, 1], [-1, 2]])
b = Matrix([[-1, 1], [-1, 0]])
a.__str__()
print()
b.__str__()
print('Результат:')
print(f'Матрицы равны: {a.__compareMatrix__(b)}')