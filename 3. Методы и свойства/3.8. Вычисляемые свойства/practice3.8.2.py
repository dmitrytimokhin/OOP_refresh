# В США и в европейских странах немного различается формат представления даты. В европейских странах принято записывать дату в формате
#
# <день> <месяц> <год>
# в Америке же сперва идет месяц, затем день и после год
#
# <месяц> <день> <год>
# Создайте класс Date, у которого есть:
#
    # конструктор __init__, принимающий 3 аргумента: день, месяц и год.
#
    # свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
#
    # свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";

class Date:
    def __init__(self, d: float, m: float, y: float):
        """

        :type y: float
        :type m: float
        :type d: float
        :param d:
        :param m:
        :param y:
        """
        self.d = str(d)
        self.m = str(m)
        self.y = str(y)
        if len(self.d) == 1:
            self.d = '0' + self.d
        if len(self.m) == 1:
            self.m = '0' + self.m
        while len(self.y) < 4:
            self.y = '0' + self.y

    @property
    def date(self) -> str:
        """

        :rtype: object
        :return:
        """
        return (f'{self.d}/{self.m}/{self.y}')

    @property
    def usa_date(self) -> str:
        """

        :rtype: object
        :return:
        """
        return (f'{self.m}-{self.d}-{self.y}')