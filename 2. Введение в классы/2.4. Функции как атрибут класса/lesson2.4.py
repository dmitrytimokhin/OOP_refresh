# Функция как атрибут класса

class Car:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def Drive() -> str:
        print("Let's go")