# Возьмите 1 - 3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы
# исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать
# прямоугольник со сторонами отрицательной длины.

class BaseException(Exception):
    pass


class NotEqualException(BaseException):
    def __str__(self) -> str:
        return "Ошибка. Матрицы не равны."


class MultiplyException(BaseException):
    def __str__(self) -> str:
        return "Ошибка. Число столбцов первой матрицы должно быть равно числу строк второй."


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
            raise NotEqualException

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
            raise NotEqualException

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
            raise MultiplyException


"""
Далее идет демонстрация работы класса.
Создание матриц, вывод в консоль.
Сложение и умножение
"""

# Раскомментировать для возбуждения ошибки при умножении матриц неправильного размера
# a = Matrix([[-1, 1, 2], [-1, 2, 1]])
# b = Matrix([[-2, 1, 3], [-2, 2, 3]])
# print('Пробуем перемножить матрицы:')
# a.__str__()
# print()
# b.__str__()
# a.__matMult__(b).__str__()

# Раскомментировать для возбуждения ошибки неравенстрва размеров матриц
print()
a = Matrix([[-1, 1], [-1, 2]])
b = Matrix([[-2, 1, 3], [-2, 2, 3]])
print()
a.__str__()
print()
b.__str__()
print(f'Сравним, равны ли матрицы: {a.__compareMatrix__(b)}')