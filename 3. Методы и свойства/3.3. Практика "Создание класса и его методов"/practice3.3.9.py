# Треугольники
# Создайте класс Triangle, в котором реализованы следующие методы
#
    # метод __init__, принимающий три стороны треугольника
#
    # метод is_exists, который отвечает на вопрос существует ли треугольник с текущими сторонами
# Треугольник существует, если каждая сторона треугольника меньше суммы двух других сторон.
    # метод is_equilateral, который проверяет является ли треугольник равносторонним
# Треугольник называется равносторонним, если у него все стороны равны
    # метод is_isosceles, который проверяет является ли треугольник равнобедренным и существующим.
# Треугольник называется равнобедренным, если у него две стороны равны

class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self) -> bool:
        self.exists = True if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b else False
        return self.exists

    def is_equilateral(self) -> bool:
        return True if (self.a == self.b == self.c) and self.exists else False

    def is_isosceles(self) -> bool:
        return True if (self.a == self.b or self.a == self.c or self.b == self.c) and self.exists else False