from abc import ABCMeta, abstractmethod, abstractproperty

class IRpcNetworking():
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        """ Run networking """

    @abstractmethod
    def stop(self):
        """ Stop networking """

    @abstractmethod
    def bind(self, address: str):
        """ Bind address """