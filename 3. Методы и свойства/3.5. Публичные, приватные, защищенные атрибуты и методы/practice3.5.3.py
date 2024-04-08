# Создайте класс Student, у которого есть:
#
    # конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;
#
    # приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
    # метод access_private_method, который вызывает приватный метод __display_details.

class Student:
    def __init__(self, name: object, age: int, branch: object):
        """

        :type branch: object
        :type age: int
        :type name: object
        :param name:
        :param age:
        :param branch:
        :rtype: object

        """

        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self) -> str:
        """

        """
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Направление: {self.__branch}')

    def access_private_method(self) -> object:
        """

        :return:
        """
        return self.__display_details()