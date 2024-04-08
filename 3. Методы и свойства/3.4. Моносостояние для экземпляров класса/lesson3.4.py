# Моносостосяние для всех экземпляров
## Когда при изменении состояния атриббута, я хочу чтобы все другие атриббуты тоже поменялись

class Cat:
    __shared_attrs = {
        'breed':'pers',
        'color':'black'
    }

    def __init__(self):
        """

        """
        self.__dict__ = Cat.__shared_attrs