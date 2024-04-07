# Property, getter-метод и setter-метод

class BankAccount:

    def __init__(self, name: object, balance: float) -> None:
        """

        :type balance: float
        :type name: object
        """
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int,float)):
            raise ValueError('Баланс должен быть число')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)