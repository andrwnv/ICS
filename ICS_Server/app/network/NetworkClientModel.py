from copy import deepcopy
import sys


class NetworkClientModel(object):
    def __init__(self):
        pass

    def do_smth(self) -> str:
        print('do_smth called')
        return 'do_smth called'

    def echo(self, text: str):
        print(text)