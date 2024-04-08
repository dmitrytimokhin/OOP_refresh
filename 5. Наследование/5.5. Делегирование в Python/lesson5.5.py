# Наследование Делегирование Delegateing

class Person:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.age = 50
    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def __init__(self,name,surname,age):
        super().__init__(name,surname)
        self.age = age

    def breathe(self):
        print('Доктор дышит')
        super().breathe()