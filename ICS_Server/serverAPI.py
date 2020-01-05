from __future__ import print_function
from server import Server

import sys
import zerorpc


class ServerAPI(object):
    def __init__(self):
        self.__server = Server()
        print('Server API created \n')

    def do_something(self) -> str:
        return self.__server.do_something()

    def echo(self, text: str):
        print(text + '\n')


def get_port() -> str:
    port = 4242

    try:
        port = int(sys.argv[1])
    except Exception as ex:
        pass

    return '{}'.format(port)


if __name__ == '__main__':
    addr = 'tcp://127.0.0.1:' + get_port()

    server = zerorpc.Server(ServerAPI())
    server.bind(addr)

    print('server start on {}\n'.format(addr))

    server.run()
