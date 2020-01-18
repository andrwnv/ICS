from configuration.FileConfigurationManager import FileConfigurationManager

from copy import deepcopy
import sys


class NetworkConfigurations:
    def __init__(self):
        config = FileConfigurationManager()

        self.__ip: str = config.value('NETWORK', 'Ip')
        self.__port: str = config.value('NETWORK', 'Port')

        self.__full_address = self.__ip + ':' + self.__port

    def get_port(self) -> str:
        return deepcopy(self.__port)

    def get_ip(self) -> str:
        return deepcopy(self.__ip)

    def get_full_address(self) -> str:
        return deepcopy(self.__full_address)

    def set_port(self, port: str) -> None:
        self.__port = deepcopy(port)

    def set_ip(self, ip: str) -> None:
        self.__ip = deepcopy(ip)

    def set_full_address(self, address: str) -> None:
        self.__full_address = deepcopy(address)
