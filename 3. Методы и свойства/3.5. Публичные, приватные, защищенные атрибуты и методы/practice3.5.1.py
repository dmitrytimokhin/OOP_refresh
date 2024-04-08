# В коде из предыдущего урока возникала ошибка:
#
# AttributeError: 'AverageCalculator' object has no attribute '__calculate_average'
# Мы не можем напрямую обращаться к приватному методу. Но есть способ, как осуществить такой доступ, мы разобрали его на лекции к этому уроку.
#
# В последней строчке кода используйте эти знания, чтобы вызвать приватный метод вне класса.

class AverageCalculator:
    def __init__(self, numbers: list):
        """

        :type numbers: list
        :param numbers:
        """
        self.numbers = numbers

    def __calculate_average(self) -> float:
        """

        :return:
        """
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator._AverageCalculator__calculate_average())