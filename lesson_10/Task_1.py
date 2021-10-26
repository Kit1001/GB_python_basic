"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.content = list_of_lists
        self.rows = len(list_of_lists)
        self.columns = len(list_of_lists[0])

    def __str__(self):
        result = []
        for row in self.content:
            result_line = []
            for column in row:
                result_line.append(f'{column: 6}')
            result_line.append('\n')
            result.append(''.join(result_line))
        return ''.join(result)

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            matrix_sum = [
                [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                for row_1, row_2 in zip(self.content, other.content)]
            return Matrix(matrix_sum)
        else:
            msg = 'Складывать можно только матрицы с одинаковой размерностью'
            raise ValueError(msg)


some_matrix_1 = [
    [3, 5, 8, 3],
    [8, -3, 7, 1]
]

some_matrix_2 = [
   [1, 4, 3, 3],
   [15, 0, -8, 11],
]

my_matrix_1 = Matrix(some_matrix_1)
my_matrix_2 = Matrix(some_matrix_2)

print('Матрица №1')
print(my_matrix_1)
print('Матрица №2')
print(my_matrix_2)

print('Сумма матриц 1 и 2:')
print(my_matrix_1 + my_matrix_2)
