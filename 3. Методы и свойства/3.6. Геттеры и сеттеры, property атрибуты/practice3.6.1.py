# Создайте класс BankAccount, который имеет следующие методы:
#
    # метод __init__, который устанавливает значения атрибутов _account_number  и _balance: номер счета и баланс
#
    # геттер-метод для атрибута _account_number
#
    # геттер-метод для атрибута _balance
#
    # сеттер-метод для атрибута _balance

class BankAccount:

    def __init__(self, account_number: int, balance: float):
        """

        :type balance: float
        :type account_number: int
        :param account_number:
        :param balance:
        """
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self) -> object:
        """ Геттер-метод для атрибута _account_number """
        return self._account_number

    def get_balance(self) -> object:
        """ Геттер-метод для атрибута _balance """
        return self._balance