# Вычесляемые property

class Square:
    def __init__(self, s: float):
        """

        :type s: float
        :param s:
        """
        self.__side = s
        self.__area = None

    @property
    def side(self) -> float:
        """

        :return:
        """
        return self.__side

    @side.setter
    def side(self, value: float):
        """

        :type value: object
        :param value:
        """
        self.__side = value
        self.__area = None

    @property
    def area(self) -> float:
        """

        :return:
        """
        if self.__area is None:
            print('calculate area')
            self.__area = self.side**2
        return self.__area