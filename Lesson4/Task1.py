# Напишите функцию для транспонирования матрицы

def generate_matrix(rows, cols: int) -> list:
    """
    Функция генерации матрицы, заполненной случайными числами
    :param rows: число строк генерируемой матрицы
    :param cols: число колонок генерируемой матрицы
    :return: matrix - сгенерированная матрица
    """

    from random import randint

    matrix = [[randint(0, 20) for _ in range(cols)] for _ in range(rows)]
    return matrix


def transpose_matrix(matrix: list) -> list:
    """
    Функция для транспонирования переданной матрицы
    :param matrix: передаваемая матрица для транспонирования
    :return: result - транспонированная матрица
    """
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


input_mat = generate_matrix(3, 4)
print("Исходная матрица:")
print(*input_mat, sep='\n')
print()
t_mat = transpose_matrix(input_mat)
print("Транспонированная матрица:")
print(*t_mat, sep='\n')
