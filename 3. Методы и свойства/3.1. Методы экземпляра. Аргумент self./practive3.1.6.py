# Создайте класс Point. У этого класса должны быть:
#
    # Метод set_coordinates, который принимает координаты точки на плоскости и сохраняет их в экземпляр класса в атрибуты x и y
#
    # Метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point, необходимо вывести сообщение "Передана не точка".

from math import sqrt

class Point:

    def set_coordinates(self, x: float, y: float):
        """
        The method saves the coordinate of the points to an instance of the class
        :param x: coordinate of the X
        :param y: coordinate of the Y
        """
        self.x = x
        self.y = y

    def get_distance(self, point: object) -> object:
        """
        The method calculates distance between two points
        :param point: instance of the Point class
        :return:
        """
        if isinstance(point, Point):
            return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        else:
            print('Передана не точка')

# Код ниже не удаляйте, он нужен для проверок
p1 = Point()
p2 = Point()
assert isinstance(p1, Point)
assert isinstance(p2, Point)

p1.set_coordinates(1, 2)
assert p1.x == 1
assert p1.y == 2
p2.set_coordinates(4, 6)
assert p2.x == 4
assert p2.y == 6
assert p1.get_distance(p2) == 5.0
p3 = Point()
p3.set_coordinates(10, 10)
p1.set_coordinates(4, 2)
assert p1.get_distance(p3) == 10.0
res = p1.get_distance(10)  # Распечатает "Передана не точка", вернет None
assert res is None, 'Метод get_distance должен возвращать None, если в него была передана не точка'

assert p2.get_distance([1, 2, 3]) is None  # Распечатает "Передана не точка", вернет None