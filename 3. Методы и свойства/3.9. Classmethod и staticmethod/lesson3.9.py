# classmethod и staticmethod

class Example:
    def hello(): # <- Можем вызвать от класса, но не можем вызвать от ЭК
        print('hello')

    def instance_hello(self): # <- Не можем вызвать от класса, но можем вызвать от ЭК
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello(): # <- Можем вызывать и от класса и от ЭК (ни к чему не привязывается), то есть можем реализовать внутри класса, не вынося за вне класса как статичную
        print('static_hello')

    @classmethod # Когда хотим делать обработку не над экземплярами, а над целым классом вместе. Здесь нам доступен наш класс со всеми его атрибутами
    def class_hello(cls): # <- Также можем вызвать от класса и от ЭК
        print(f'instance_hello {cls}')