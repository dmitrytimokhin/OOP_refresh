# Практика. Класс Point(x,y)
from math import sqrt

class Point:

    list_points = []

    def __init__(self, coord_x: float = 0, coord_y: float = 0) -> object:
        """

        :type coord_y: float
        :type coord_x: float
        :param coord_x:
        :param coord_y:
        """
        self.move_to(coord_x,coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x: float, new_y: float) -> object:
        """

        :type new_y: object
        :type new_x: object
        :param new_x:
        :param new_y:
        """
        self.x = new_x
        self.y = new_y

    def go_home(self):
        """

        """
        self.move_to(0,0)
        
    def print_point(self) -> str:
        """

        """
        print(f"Точка с координатами ({self.x},{self.y})")

    def calc_distance(self, another_point: object) -> float:
        """

        :param another_point:
        """
        if isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)