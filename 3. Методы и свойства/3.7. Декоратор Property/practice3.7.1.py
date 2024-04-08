# Создайте класс Celsius, который представляет температуру в градусах Цельсия. Основная задача класса - предоставить возможность конвертировать температуру из градусов Цельсия в градусы Фаренгейта, а также обеспечить контроль за корректностью введенных значений.
#
#  Класс Celsius, должен иметь:
#
    # метод __init__, который принимает значение температуры в градусах по Цельсию и сохраняет в атрибут экземпляра.
#
    # метод to_fahrenheit, который выполняет конвертацию температуры из градусов Цельсия в градусы Фаренгейта по формуле
#
# °F = (°C × 9/5) + 32
#
# и возвращает результат этой конвертации.
#
    # свойство-геттер temperature, которое предоставляет доступ к значению температуры
#
    # свойство-сеттер temperature, которое выполняется при установке нового значения температуры. Если значение меньше -273.15 градусов Цельсия (абсолютный ноль), вызывается исключение ValueError. В противном случае, происходит установка нового значения температуры.

# Напишите определение класса Celsius
class Celsius:
    def __init__(self, cels_temp: float):
        """

        :type cels_temp: object
        :param cels_temp:
        """
        self.cels_temp = cels_temp

    def to_fahrenheit(self) -> float:
        """

        :return:
        """
        return (self.cels_temp * 9 / 5) + 32

    @property
    def temperature(self) -> float:
        """

        :return:
        """
        return self.cels_temp

    @temperature.setter
    def temperature(self, value: float):
        """

        :param value:
        """
        if value < -273.15:
            raise ValueError
        self.cels_temp = value


# Ниже код для проверки методов класса Celsius

celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0

print('Good')