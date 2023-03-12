# Task_1

# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def get_triangle_sides():
    """Мспользуется для получения размеров сторон треугольника от пользователя

        Note:
            Возможны проблемы кастом во float введенного пользователем значения

    """

    sides = []
    for i in range(3):
        sides.append(float(input(f'Введите длину {i + 1} стороны треугольника и нажмите "Enter".\n')))
    return sides


def check_triangle_exist(sides_values: list) -> bool:
    """Мспользуется для проверки возможности существования треугольника в зависимости от переданных размеров

        Parameters
        ----------
        sides_values : list
            список размеров сторон треугольника
    """

    triangle_exists = True
    if (sides_values[0] + sides_values[1]) < sides_values[2]:
        triangle_exists = False
    if (sides_values[1] + sides_values[2]) < sides_values[0]:
        triangle_exists = False
    if (sides_values[0] + sides_values[2]) < sides_values[1]:
        triangle_exists = False
    return triangle_exists


def define_triangle_kind(sides_values: list) -> str:
    """Мспользуется для определения является ли треугольник разносторонним, равнобедренным или равносторонним

        Parameters
        ----------
        sides_values : list
            список размеров сторон треугольника
    """

    if sides_values[0] == sides_values[1] == sides_values[2]:
        triangle_kind = "Треугольник равносторонний."
    elif sides_values[0] == sides_values[1] or sides_values[0] == sides_values[2] or sides_values[1] == sides_values[2]:
        triangle_kind = "Треугольник равнобедренный."
    else:
        triangle_kind = "Треугольник разносторонний."
    return triangle_kind


triangle_sides = get_triangle_sides()
if check_triangle_exist(triangle_sides):
    print(f'Треугольник со сторонами {[*triangle_sides]} существует.')
    print(define_triangle_kind(triangle_sides))
else:
    print(f'Треугольник со сторонами {[*triangle_sides]} НЕ существует.')