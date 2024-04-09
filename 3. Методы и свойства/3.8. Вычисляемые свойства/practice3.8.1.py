# Создайте класс Rectangle, у которого есть:
#
    # конструктор __init__, принимающий 2 аргумента: длину и ширину.
    # свойство area, которое возвращает площадь прямоугольника;

class Rectangle:
    def __init__(self, l: float, w: float):
        """

        :type l: float
        :type w: float
        :param l:
        :param w:
        """
        self.l = l
        self.w = w

    @property
    def area(self) -> float:
        """

        :return:
        """
        return self.l * self.w