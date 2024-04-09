# Перед вами — реализация класса RobotVacuumCleaner. Сейчас над каждым методом стоит знак _.
#
# Ваша задача сделать код корректным: для это нужно заменить знак _ на один из декораторов @staticmethod, @classmethod и @property или же просто удалить знак

class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    @classmethod
    def update_charge(cls, new_value: float):
        """

        :type new_value: object
        :param new_value: 
        """
        cls.charge = new_value

    @staticmethod
    def hello(name: str) -> str:
        """

        :rtype: object
        :type name: object
        :param name: 
        :return: 
        """
        return f'Привет, {name}'

    @property
    def data(self) -> dict:
        """

        :rtype: dict
        :return: 
        """
        return {
            'name': self.name,
            'charge': self.charge
        }

    def make_clean(self) -> str:
        """

        :rtype: str
        :return: 
        """
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'