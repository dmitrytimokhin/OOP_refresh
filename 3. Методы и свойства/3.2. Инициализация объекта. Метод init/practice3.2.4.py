# Создайте класс SoccerPlayer, у которого есть:
#
    # Конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо создать 2 атрибута экземпляра: goals и assists — общее количество голов и передач игрока, изначально оба значения должны быть 0.
#
#    Метод score, который принимает количество голов, забитых игроком. По умолчанию данное значение равно единице. Метод должен увеличить общее количество забитых голов игрока на переданное значение.
#
    # Метод make_assist, который принимает количество передач, сделанных игроком за матч. По умолчанию данное значение равно единице. Метод должен увеличить общее количество сделанных передач игроком на переданное значение.
#
    # Метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>

# Напишите определение класса SoccerPlayer
class SoccerPlayer:
    def __init__(self,
                 name:object=None,
                 surname:object=None,
                 goals:int=0,
                 assists:int=0):

        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self,goals:int=1):
        self.goals = self.goals + goals

    def make_assist(self,assists:int=1):
        self.assists = self.assists + assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

# Ниже код для проверки методов класса SoccerPlayer
leo = SoccerPlayer('Leo', 'Messi')
assert isinstance(leo, SoccerPlayer)
assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
leo.score(700)
assert leo.goals == 700
leo.make_assist(500)
assert leo.assists == 500

leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')
assert isinstance(kokorin, SoccerPlayer)
assert kokorin.name == 'Alex'
assert kokorin.surname == 'Kokorin'
assert kokorin.assists == 0
assert kokorin.goals == 0
kokorin.score()
assert kokorin.goals == 1
kokorin.score(5)
assert kokorin.goals == 6
kokorin.make_assist()
assert kokorin.assists == 1
kokorin.make_assist(10)
assert kokorin.assists == 11

kokorin.statistics()


obi = SoccerPlayer('Оби-Ван', 'Кеноби')
obi.make_assist()
assert obi.name == 'Оби-Ван'
assert obi.surname == 'Кеноби'
assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
obi.statistics()

mila = SoccerPlayer('Mila', 'Kunis')
mila.make_assist()
mila.statistics()