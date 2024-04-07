#  Создайте класс Vehicle, у которого есть:
#
    # Конструктор __init__, принимающий максимальную скорость и пробег. Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно.
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)# 240 18
# Ваша задача только определить класс Vehicle

class Vehicle:

    def __init__(self, max_speed: float, mileage: float):
        """
The creation of the class Venicle
        :param max_speed: max speed of the vehicle
        :param mileage: mileage of the vehicle
        """

        self.max_speed = max_speed
        self.mileage = mileage


# Ниже расположен код для проверок, его не нужно удалять
modelX = Vehicle(200, 18000)
assert modelX.max_speed == 200
assert modelX.mileage == 18000
assert modelX.__dict__ == {'max_speed': 200, 'mileage': 18000}

audi = Vehicle(240, 5)
assert audi.__dict__ == {'max_speed': 240, 'mileage': 5}
print('Good')