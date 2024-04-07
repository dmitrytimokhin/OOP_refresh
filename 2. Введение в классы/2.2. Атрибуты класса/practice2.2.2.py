# Перед нами все тот же класс Book, но теперь ваша задача получить доступ к атрибутам writer и pages при помощи функции getattr
#
# Сначала выведите атрибут writer, затем на новой строке pages

class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

#print(getattr(Book, 'writer'))
#print(getattr(Book, 'pages'))