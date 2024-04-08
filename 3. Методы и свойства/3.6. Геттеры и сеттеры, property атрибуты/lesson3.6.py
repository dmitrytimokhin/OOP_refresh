# Property, getter-метод и setter-метод

class BankAccount:

    def __init__(self, name: object, balance: float):
        """

        :type balance: float
        :type name: object
        """
        self.name = name
        self.__balance = balance

    def get_balance(self) -> float:
        """

        :return:
        """
        print('get balance')
        return self.__balance

    def set_balance(self, value: float) -> str:
        """

        :type value: object
        :param value:
        """
        print('set balance')
        if not isinstance(value, (int,float)):
            raise ValueError('Баланс должен быть число')
        self.__balance = value

    def delete_balance(self) -> str:
        """

        """
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)