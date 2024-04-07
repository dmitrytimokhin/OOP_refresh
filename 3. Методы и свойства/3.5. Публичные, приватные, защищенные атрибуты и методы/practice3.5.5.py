# Создайте класс Library, который имеет следующие методы:
#
    # метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.
#
    # приватный метод check_availability, который принимает название книги и возвращает True, если книга присутствует в библиотеке, в противном случае возвращается False.
#
    # публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода check_availability. Возвращает True, если нашел,  иначе False.
#
    # публичный метод return_book, который принимает название книги, которую нужно вернуть в библиотеку (добавить в конец атрибута __books), ничего возвращать не нужно.
#
    # защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в наличии, ее необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть True , как знак того, что операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False.

class Library:

    def __init__(self, books: list) -> None:
        """

        :type books: list
        :rtype: object
        :param list_of_books:
        """

        self.__books = books

    def __check_availability(self, name: str) -> bool:
        """

        :rtype: object
        :type name: str
        :param name: 
        :return: 
        """
        return name in self.__books

    def search_book(self, name: str) -> bool:
        """

        :type name: str
        :rtype: bool
        :param name: 
        :return: 
        """
        return self.__check_availability(name)

    def return_book(self, name: str) -> None:
        """

        :type name: str
        :param name: 
        """
        self.__books.append(name)

    def _checkout_book(self, name: str) -> bool:
        """

        :type name: str
        :rtype: bool
        :param name: 
        :return: 
        """
        if name in self.__books:
            self.__books.remove(name)
            return True
        else:
            return False



