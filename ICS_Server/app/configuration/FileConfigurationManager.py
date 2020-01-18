from configuration.IConfigurable import IConfigurable

import configparser


class FileConfigurationManager(IConfigurable, object):
    """
        Class that implements saving parameters in ini file.
    """

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__config_file_path = 'ics_server.ini'
            cls.__config = configparser.ConfigParser()

            # init default params
            cls.__config['NETWORK'] = {
                'Port': '4545',
                'Ip': 'tcp://127.0.0.1'
            }

            with open(cls.__config_file_path, 'w') as config_file:
                cls.__config.write(config_file)

            cls.__instance = super(FileConfigurationManager, cls).__new__(cls)

        return cls.__instance

    def sync(self) -> None:
        with open(self.__config_file_path, 'r') as output:
            pass  # TODO: update all params

    def set_value(self, category: str, field: str, value: str) -> None:
        self.__config[category][field] = value

        with open(self.__config_file_path, 'w') as config_file:
            self.__config.write(config_file)

    def value(self, category: str, field: str) -> str:
        return self.__config[category][field]
