# Ниже определен пустой класс SuperHero. Ваша задача: создать два ЭК и сохранить их в переменные batman и superman
#
# Для ЭК, хранящегося в переменной batman, необходимо создать
#
# атрибут can_fly со значением False
# атрибут damage со значением 175
# Для ЭК, хранящегося в переменной superman, необходимо создать
#
# атрибут can_fly со значением True
# атрибут damage со значением 285
# атрибут alter_ego со значением 'Кларк Кент'
# Ничего выводить на экран в этом задании не требуется

class SuperHero:
    pass


batman = SuperHero()
batman.can_fly = False
batman.damage = 175

superman = SuperHero()
superman.can_fly = True
superman.damage = 285
superman.alter_ego = "Кларк Кент"