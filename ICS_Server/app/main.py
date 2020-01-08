from __future__ import print_function

import sys
import zerorpc

from network.NetworkConfigurations import NetworkConfigurations
from network.RpcNetworking import RpcNetworking
from network.RpcMethods import RpcMethods

if __name__ == '__main__':
    rpc_networking = RpcNetworking()

    print('----- server start ----- \n')
    rpc_networking.run()