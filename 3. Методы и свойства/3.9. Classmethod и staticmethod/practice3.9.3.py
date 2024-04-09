#  Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:
#
    # класс-метод from_diameter, принимающий диаметр круга. Метод from_diameter должен возвращать новый экземпляр класса Circle(учитывайте, что экземпляры круга создаются по радиусу);
#
    # статик-метод is_positive, принимающий одно число. Метод is_positive должен возвращать ответ, является ли переданное число положительным;
#
    # статик-метод area, который принимает радиус и возвращает площадь круга. Для этого воспользуйтесь формулой: pi∗r^2
#   и в качестве значения pi возьмите 3.14
# Ваша задача только добавить реализацию трех методов в класс Circle

class Circle:

    def __init__(self, radius: float):
        """

        :type radius: object
        :param radius: 
        """
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, d: float) -> float:
        """

        :rtype: float
        :type d: float
        :param d: 
        :return: 
        """
        return cls(d / 2)

    @staticmethod
    def is_positive(value: float) -> float:
        """

        :rtype: object
        :type value: object
        :param value: 
        :return: 
        """
        if value >= 0:
            return value

    @staticmethod
    def area(radius: float) -> float:
        """

        :rtype: object
        :type radius: object
        :param radius: 
        :return: 
        """
        return 3.14 * (radius ** 2)