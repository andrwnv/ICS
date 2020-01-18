from network.RpcNetworking import RpcNetworking

if __name__ == '__main__':
    rpc_networking = RpcNetworking()

    print('----- server start ----- \n')
    rpc_networking.run()
