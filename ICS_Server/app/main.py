from __future__ import print_function

import sys
import zerorpc

from network.RpcNetworking import RpcNetworking
from network.NetworkConfigurations import NetworkConfigurations
from network.RpcMethods import RpcMethods

if __name__ == '__main__':
    rpc_networking = RpcNetworking()
    rpc_networking.run()

    print('----- server start ----- \n')