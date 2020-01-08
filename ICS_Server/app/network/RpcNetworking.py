from network.NetworkConfigurations import NetworkConfigurations
from network.IRpcNetworking import IRpcNetworking
from network.RpcMethods import RpcMethods

from zerorpc import Server

from multiprocessing import Process

import threading

class RpcNetworking(IRpcNetworking):
    def __init__(self):
        self.__rpc_server = Server(RpcMethods())
        self.__config = NetworkConfigurations()
        self.__server_process = None

    def run(self):
        self.__server_process = Process(target=self.__rpc_server.run)
        self.__server_process.start()

    def stop(self): 
        if self.__server_process is not None:
            self.__server_process.terminate()  # TODO: try catch block

    def __bind(self): 
        self.__rpc_server.bind(self.__config.get_full_address())


assert issubclass(RpcNetworking, IRpcNetworking)
assert isinstance(RpcNetworking(), IRpcNetworking)