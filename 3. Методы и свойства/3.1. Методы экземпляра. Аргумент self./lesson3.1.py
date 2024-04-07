# Методы экземпляра

class Cat():
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'My breed is {instance.breed}')

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'My name is {instance.name}')
        else:
            print('nothing')

    def set_value(koshka, value):
        koshka.name = value

# В классике вместо "instance" прописывается "self"
