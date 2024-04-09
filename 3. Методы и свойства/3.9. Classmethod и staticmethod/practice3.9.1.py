# Физики заказали вам создать несколько функций, которые помогают конвертировать температуру из градусов по Цельсию в градусы по Кельвину и по Фаренгейту. Но так как все эти функции работают с температурами, мы решаем объединить их в один класс TemperatureConverter
#
# Создайте класс TemperatureConverter, который имеет следующие методы:
#
#  статический метод celsius_to_fahrenheit, который принимает температуру в градусах Цельсия и переводит ее в градусы по Фаренгейту, используя следующую формулу:
#
# статический метод fahrenheit_to_celsius, который принимает температуру в градусах по Фаренгейту и переводит ее в градусы Цельсия, используя следующую формулу:
#
# статический метод celsius_to_kelvin, который переводит из Цельсия в Кельвин путем прибавления значения 273.15
#
# статический метод kelvin_to_celsius, который переводит из Кельвин в градусы по Цельсию путем уменьшения значения на 273.15
#
# два статических метода fahrenheit_to_kelvin и kelvin_to_fahrenheit, выполняющих преобразование градусов по Фаренгейту в Кельвины и наоборот. Рассчитываются они по следующим формулам

# статический метод format, принимающий значение градусов и один из символов K, F, C. Возвращает строку с красивым отображением градусов в указанной единице измерения.
    # F соответствует °F
#
    # C соответствует °C
#
    # K соответствует °K

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        """

        :rtype: float
        :type c: float
        :param c: 
        :return: 
        """
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        """

        :rtype: float
        :type f: float
        :param f: 
        :return: 
        """
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(c: float) -> float:
        """

        :rtype: float
        :type c: float
        :param c: 
        :return: 
        """
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k: float) -> float:
        """

        :rtype: float
        :type k: float
        :param k: 
        :return: 
        """
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f: float) -> float:
        """

        :rtype: float
        :type f: float
        :param f: 
        :return: 
        """
        return round(((5 / 9 * (f - 32)) + 273.15), 2)

    @staticmethod
    def kelvin_to_fahrenheit(k: float) -> float:
        """

        :rtype: float
        :type k: float
        :param k: 
        :return: 
        """
        return round(((9 / 5 * (k - 273.15)) + 32), 2)

    @staticmethod
    def format(temp: float, t_format: str) -> str:
        """

        :rtype: str
        :type t_format: str
        :type temp: float
        :param temp:
        :param t_format:
        :return:
        """
        if t_format == 'F':
            return f'{temp}°F'
        elif t_format == 'K':
            return f'{temp}°K'
        elif t_format == 'C':
            return f'{temp}°C'