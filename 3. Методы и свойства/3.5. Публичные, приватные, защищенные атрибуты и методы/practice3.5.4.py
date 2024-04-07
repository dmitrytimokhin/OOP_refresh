# Создайте класс BankDeposit, который имеет следующие методы:
#
    # метод __init__, который устанавливает значения атрибутов name, balance и rate: владелец депозита, значение депозита и годовая процентная ставка.
#
    # приватный метод __calculate_profit, который возвращает количество денег, которое заработает владелец счета через год с учетом его годовой ставки.
#
    # публичный метод get_balance_with_profit, который возвращает общее количество средств, которое будет у владельца депозита через год.

class BankDeposit:

    def __init__(self, name: object, balance: float, rate: float) -> None:
        """

        :type rate: float
        :type balance: float
        :type name: object
        :rtype: object
        :param name:
        :param balance:
        :param rate:
        """
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self) -> float:
        """

        :return:
        """
        return self.balance*(self.rate)/100

    def get_balance_with_profit(self) -> float:
        """

        :return:
        """
        return self.balance + self.__calculate_profit()