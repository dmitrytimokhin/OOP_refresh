# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы «Полоска белая», «Полоска черная» без кавычек, начиная именно с фразы «Полоска белая».
#
# Также реализуйте метод run_away, который печатает фразу «Oh, Sugar Honey Ice Tea». Взгляните откуда взялась эта фраза

class Zebra:
    def __init__(self):
        self.n = 1
        self.string_to_print1 = 'белая'
        self.string_to_print2 = 'черная'

    def which_stripe(self):
        if self.n&1==1:
            print(f'Полоска {self.string_to_print1}')
        else:
            print(f'Полоска {self.string_to_print2}')
        self.n+=1

    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')
