from network.NetworkConfigurations import NetworkConfigurations
from network.IRpcNetworking import IRpcNetworking
from network.RpcMethods import RpcMethods

from zerorpc import Server

from multiprocessing import Process

import gevent

class RpcNetworking(IRpcNetworking):
    def __init__(self):
        self.__rpc_server = Server(RpcMethods())
        self.__config = NetworkConfigurations()
        self.__server_process = None

    def run(self):
        self.__bind()
        self.__rpc_server.run()

    def __bind(self): 
        self.__rpc_server.bind(self.__config.get_full_address())


assert issubclass(RpcNetworking, IRpcNetworking)
assert isinstance(RpcNetworking(), IRpcNetworking)