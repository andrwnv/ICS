from copy import deepcopy
import sys


class NetworkClientModel(object):
    """
        Class that describe possible RPC interactions between server and client.
    """

    def __init__(self):
        pass

    def echo(self, text: str) -> str:
        print(text)
        return text