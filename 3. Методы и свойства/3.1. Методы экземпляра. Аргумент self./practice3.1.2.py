#  Создайте класс Robot, в котором реализованы:
#
    # Метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
#
    # Метод say_bye ,  печатающий на экран фразу «See u later alligator»
# После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
#
# Затем вызовите у переменной  c3po  метод say_hello , а затем метод say_bye
#
# И то же самое сделайте с переменной r2d2:  вызовите метод say_hello , потом — метод say_bye

class Robot:

    def say_hello(self):
        print('Hello, human! My name is C-3PO')

    def say_bye(self):
        print('See u later alligator')


c3po = Robot()
r2d2 = Robot()

c3po.say_hello()
c3po.say_bye()

r2d2.say_hello()
r2d2.say_bye()