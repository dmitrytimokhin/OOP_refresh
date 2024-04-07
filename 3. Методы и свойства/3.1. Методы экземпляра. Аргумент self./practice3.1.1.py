# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
#
    # Необходимо написать только определение класса
#
# Пример работы с классом Lion
#
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!

# Напишите определение класса Lion
class Lion:
    voice = ''

    def roar(self):
        self.voice = 'Rrrrrrr!!!'
        print(self.voice)


# Ниже код для проверки класса Lion
s = Lion()
assert isinstance(s, Lion)
assert s.__dict__ == {}
s.roar()