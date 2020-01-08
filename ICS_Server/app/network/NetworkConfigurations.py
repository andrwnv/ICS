from copy import deepcopy
import sys


class NetworkConfigurations():
    def __init__(self):
        self.__ip: str = 'tcp://127.0.0.1'
        self.__port: str = self.get_port()

        self.__full_address = self.__ip + ':' + self.__port


    def get_port(self) -> str:
        port: int = 4242

        try:
            port = int(sys.argv[1])
        except Exception as ex:
            pass

        return '{}'.format(port)


    def get_ip(self):
        return deepcopy(self.__addr)


    def get_full_address(self):
        return deepcopy(self.__full_address)