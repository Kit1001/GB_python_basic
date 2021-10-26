"""
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).

Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и округление до целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, nucleus_num):
        self.nucleus_num = nucleus_num

    def __add__(self, other):
        if type(other) == Cell:
            return Cell(self.nucleus_num + other.nucleus_num)
        else:
            msg = 'Операция возможна только между клетками'
            raise TypeError(msg)

    def __sub__(self, other):
        if type(other) == Cell:
            if self.nucleus_num < other.nucleus_num:
                msg = "Операция возможна только если в первой клетке ячеек больше, чем во второй"
                raise ValueError(msg)
            else:
                return Cell(self.nucleus_num - other.nucleus_num)
        else:
            msg = 'Операция возможна только между клетками'
            raise TypeError(msg)

    def __mul__(self, other):
        if type(other) == Cell:
            return Cell(self.nucleus_num * other.nucleus_num)
        else:
            msg = 'Операция возможна только между клетками'
            raise TypeError(msg)

    def __floordiv__(self, other):
        if type(other) == Cell:
            return Cell(self.nucleus_num // other.nucleus_num)
        else:
            msg = 'Операция возможна только между клетками'
            raise TypeError(msg)

    def make_order(self, num_in_row):
        cycles = self.nucleus_num // num_in_row
        leftovers = self.nucleus_num % num_in_row

        string = []
        for _ in range(cycles):
            for _ in range(num_in_row):
                string.append('*')
            string.append('\n')
        for _ in range(leftovers):
            string.append('*')

        if leftovers == 0:
            string.pop()

        return ''.join(string)


cell_a = Cell(30)
cell_b = Cell(10)

print('Сложение клеток: \n', (cell_a + cell_b).nucleus_num, sep='')
print('Вычитание клеток: \n', (cell_a - cell_b).nucleus_num, sep='')
print('Умножение клеток: \n', (cell_a * cell_b).nucleus_num, sep='')
print('Деление клеток: \n', (cell_a // cell_b).nucleus_num, sep='')

print('Метод .make_order(6) для клетки из 30 ячеек:\n', repr(cell_a.make_order(6)), sep='')

print('Метод .make_order(9) для клетки из 30 ячеек:\n', repr(cell_a.make_order(9)), sep='')
