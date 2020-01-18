from configuration.NetworkConfigurations import NetworkConfigurations
from network.NetworkClientModel import NetworkClientModel
from network.IRpcNetworking import IRpcNetworking

from zerorpc import Server


class RpcNetworking(IRpcNetworking):
    def __init__(self):
        self.__rpc_server = Server(NetworkClientModel())
        self.__config = NetworkConfigurations()

    def bind(self, address: str) -> None:
        self.__config.set_full_address(address)
        self.__rpc_server.bind(self.__config.get_full_address())

    def run(self) -> None:
        self.bind(self.__config.get_full_address())
        self.__rpc_server.run()

    def stop(self) -> None:
        self.__rpc_server.stop()
