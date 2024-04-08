# Public protected private attr and methods

class BankAccount:

    def __init__(self, name: object, balance: float, passport: object):
        """

        :type passport: object
        :type balance: float
        :type name: object
        :rtype: object
        :param name:
        :param balance:
        :param passport:
        """

        self.name = name #_name - protected; __name - private
        self.balance = balance #_balance - protected; __balance - private
        self.passport = passport #_passport - protected; __passport - private

        self._name = name  # _name - protected; __name - private
        self._balance = balance  # _balance - protected; __balance - private
        self._passport = passport  # _passport - protected; __passport - private

        self.__name = name #_name - protected; __name - private
        self.__balance = balance #_balance - protected; __balance - private
        self.__passport = passport #_passport - protected; __passport - private

    def print_public_data(self) -> object:
        """

        """
        print(self.name, self.balance, self.passport)


    def print_protected_data(self) -> object:
        """

        """
        print(self._name, self._balance, self._passport)

    def print_private_data(self) -> object:
        """

        """

        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 10000, 454345342345)
account1.print_public_data()
account1.print_protected_data()
account1.print_private_data()

print(dir(account1))

# Получить доступ смогу только через: account1._BankAccount__balance



