"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        img = self.imaginary if self.imaginary != 0 else ""
        return f'{self.real} + {img}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)


a = ComplexNumber(8, 0)
b = ComplexNumber(5, 3)
print('Комплексные числа a и b:')
print(a, b, sep=', ')
print('\nСумма a + b:')
print(a + b)
print('\nУмножение a * b:')
print(a * b)
