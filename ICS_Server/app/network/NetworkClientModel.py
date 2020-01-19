from copy import deepcopy
import sys


class NetworkClientModel(object):
    """
        Class that describe possible RPC interactions between server and client.
    """

    def __init__(self):
        pass

    def do_smth(self) -> str:
        print('do_smth called')
        return 'do_smth called'

    def echo(self, text: str):
        print(text)