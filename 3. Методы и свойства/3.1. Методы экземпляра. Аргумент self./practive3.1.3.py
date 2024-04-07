# В предыдущей задаче вы могли обратить внимание на то, что выводится всегда одно и то же имя робота в методе say_hello . Давайте это исправим при помощи атрибута экземпляра name . Для этого переопределяем класс Robot, в котором должны быть реализованы:
#
    # Метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name
#
    # Метод say_hello . Метод должен проверить, есть ли у ЭК атрибут name . Если атрибут name  присутствует, необходимо напечатать фразу «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени»
#
    # Метод say_bye ,  печатающий на экран фразу «See u later alligator»
# Необходимо написать только определение класса Robot

# Напишите определение класса Robot
class Robot:

    def set_name(self, name: str):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


# Ниже код для проверки класса Robot

c3po = Robot()
c3po.say_hello()
c3po.set_name('R2D2')
c3po.say_hello()
c3po.say_bye()

r = Robot()
r.set_name('Chappy')
r.say_hello()

d = Robot()
d.say_hello()
d.set_name('Wally')
d.say_hello()

