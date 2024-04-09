#    Создайте класс Money, у которого есть:
#
    # конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут экземпляра total_cents.
#
    # свойство-геттер dollars, которое возвращает количество имеющихся долларов;
#
    # свойство-сеттер dollars, которое принимает целое неотрицательное число — количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
#
    # свойство геттер cents, которое возвращает количество имеющихся центов;
#
    # свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100  количество центов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
#
    # метод __str__ (информация по данному методу), который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов". Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами

class Money:

    def __init__(self, dollars: float, cents: float):
        """

        :type cents: object
        :type dollars: object
        :param dollars: 
        :param cents: 
        """
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self) -> float:
        """

        :return: 
        """
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value: float):
        """

        :type value: object
        :param value: 
        :return: 
        """
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.total_cents % 100
        else:
            return print('Error dollars')

    @property
    def cents(self) -> float:
        """

        :rtype: float
        :return: 
        """
        return self.total_cents % 100

    @cents.setter
    def cents(self, value: float):
        """

        :type value: object
        :param value: 
        :return: 
        """
        if isinstance(value, int) and value >= 0 and value <= 99:
            self.total_cents = self.total_cents // 100 * 100 + value
        else:
            return print('Error cents')

    def __str__(self):
        """

        :return: 
        """
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"