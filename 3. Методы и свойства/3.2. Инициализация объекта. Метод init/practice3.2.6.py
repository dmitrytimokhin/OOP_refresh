#  Создайте класс Person, у которого есть:
#
    # Конструктор __init__, принимающий имя, фамилию и возраст. Их необходимо сохранить в атрибуты экземпляра first_name , last_name, age.
#
    # Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".
#
    # Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.

# Напишите определение класса Person
class Person:
    def __init__(self, first_name: str = None, last_name: str = None, age: int = None):
        """

        :type age: object
        :type last_name: object
        :type first_name: object
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self) -> str:
        """

        :return:
        """
        return (f'{self.last_name} {self.first_name}')

    def is_adult(self) -> int:
        """

        :return:
        """
        return self.age >= 18

# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True

p2 = Person('Hermione', 'Granger', 16)
assert isinstance(p2, Person)
assert p2.age == 16
assert p2.first_name == 'Hermione'
assert p2.last_name == 'Granger'
assert p2.full_name() == 'Granger Hermione'
assert p2.is_adult() is False
print('Good')