from data_base_controller import IDataBaseController

import sqlite3


class SQLiteController(IDataBaseController):
    def __init__(self):
        pass

    def connect(self) -> bool:
        return True

    def disconnect(self) -> bool:
        return True

    def fetch(self) -> []:
        return []

    def commit(self) -> bool:
        return True
