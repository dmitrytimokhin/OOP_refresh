# Ваша задача — создать класс CustomLabel, у которого есть:
#
# метод __init__, принимающий один обязательный аргумент — текст виджета, который необходимо сохранить в атрибут text. Также в метод  может поступать произвольное количество именованных аргументов. Их необходимо сохранять в атрибуты экземпляра под тем же названием.
#
# метод config, который принимает произвольное количество именованных атрибутов. Он должен создать атрибут с указанным именем или, если этот атрибут уже присутствовал в экземпляре, изменить его на новое значение
# Пример использования:
#
# label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
#
# label.config(color='red', bd=100)
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}

# Напишите определение класса CustomLabel
class CustomLabel:
    def __init__(self, text: object, **kwargs: object):
        """

        :type text: object
        :param text:
        :param kwargs:
        """
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs: object):
        """

        :param kwargs:
        """
        self.__dict__.update(**kwargs)

# Ниже код для проверки методов класса CustomLabel
label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
label2 = CustomLabel(text="Username")
label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)

assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
assert label2.__dict__ == {'text': 'Username'}
assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}

print(label1.__dict__)
print(label2.__dict__)
print(label3.__dict__)
print(label4.__dict__)
print(label5.__dict__)

label4.config(color='red', bd=100)
label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)

assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
                           'color': 'red', 'bd': 100, 'z': 432}