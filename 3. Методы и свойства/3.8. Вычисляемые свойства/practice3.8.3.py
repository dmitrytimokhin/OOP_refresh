# Создайте класс Password, который имеет:
#
    # метод __init__, который устанавливает значение атрибута password
#
    # вычисляемое свойство strength, которое определяет стойкость пароля. Если длина пароля меньше 8 символов, то такой пароль считается слабым, свойство должно вернуть строку  "Weak". Сильным паролем считается тот, в котором длина символов 12 и более, в таком случае свойство возвращает строку "Strong". Во всех остальных случаях необходимо вернуть "Medium"

class Password:
    def __init__(self, password: object):
        """

        :type password: object
        :param password: 
        """
        self.password = password

    @property
    def strength(self) -> str:
        """

        :rtype: str
        :return: 
        """
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) < 12:
            return 'Medium'
        else:
            return 'Strong'