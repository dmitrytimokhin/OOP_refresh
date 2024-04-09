# Очень часто настройки приложения выносят в отдельный файл, и при старте приложения подгружают из него значения.
#
# Вам необходимо разработать простой конфигурационный менеджер для вашего приложения. Для этого необходимо реализовать класс AppConfig, который предоставляет методы для загрузки конфигурации из JSON-файла и получения значений конкретных параметров.
#
# В классе AppConfig должно быть реализовано следующее:
#
    # метод load_config, который загружает конфигурацию из указанного JSON-файла
#
    # метод get_config, который принимает ключ и возвращает соответствующее значение из загруженной конфигурации. Если ключ не найден, метод должен возвращать None. Также необходимо предоставить возможность обращаться к вложенным параметрам через точку.
#
# Вам будет предоставлен файл 'app_config.json', который имеет следующее содержимое
#
# {
#   "database": {
#     "host": "127.0.0.1",
#     "port": 5432,
#     "database_name": "postgres_db",
#     "user": "owner",
#     "password": "ya_vorona_ya_vorona"
#   },
#   "api_key": "hUFHu834837248jhoiHF89",
#   "log_level": "debug",
#   "max_connections": 10
# }
# Необходимо реализовать возможность вызова перечисленных методов как через класс, так и через экземпляр. Также необходимо обеспечить распространение значений параметров на все экземпляры класса AppConfig. Это значит, что все экземпляры AppConfig должны иметь одинаковые значение конфигурации приложения.

import json


class AppConfig:
    config = {}

    @classmethod
    def load_config(cls, filename: object):
        """

        :type filename: object
        :param filename: 
        """
        with open(filename) as file:
            cls.config = json.load(file)

    @classmethod
    def get_config(cls, key: str):
        """

        :type key: object
        :param key: 
        :return: 
        """
        splitkey = key.split('.')
        if len(splitkey) == 1:
            return cls.config.get(splitkey[0])
        else:
            return cls.config['database'].get(splitkey[1])