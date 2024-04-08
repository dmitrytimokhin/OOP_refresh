# Создайте класс Notebook, у которого есть:
#
    # конструктор __init__, принимающий список записей, в нем могут находиться любые значения. Необходимо сохранить его в защищенном атрибуте ._notes
#
    # свойство notes_list, которое распечатает содержимое атрибута ._notes в виде пронумерованного списка дел (см. пример ниже)

class Notebook:
    def __init__(self, notes: list):
        """

        :param notes:
        """
        self._notes=notes
    @property
    def notes_list(self) -> str:
        """

        """
        for i,j in enumerate(self._notes):
            print(f'{i+1}.{self._notes[i]}')
