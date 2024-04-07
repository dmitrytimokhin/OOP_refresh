# Теперь потренируемся удалять атрибуты в классе. Для этого вам необходимо из класса Book удалить три атрибута:
#
    # pages
    # writer
    # rating
# Удаление выполните с помощью оператора del и функции delattr
#
# В этом задании ничего выводить на экран не требуется

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213
    rating = 8.7
    genre = 'dystopian'


#for i in ['pages', 'writer', 'rating']:
#    delattr(Book, i)