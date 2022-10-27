from sqlib.modules.connection import *
from sqlib.modules.insert import *
from sqlib.modules.select import *
from sqlib.modules.create import *


class Sqlib(Connection, Select, Insert, Create):
    def __init__(self, *, host: str, user: str, password: str, database: str, settings: dict = {}):
        if "port" in settings:
            self.host = f"{host}:{settings['port']}"
        super().__init__(host, user, password, database)
        self.host = host
        self.user = user
        self.password = password
        self.settings = settings


    # def select(self, table: str, columns: list, where: dict = None, limit: int = None):
    #     return super().select(table, columns, where, limit)



    def __str__(self) -> str:
        return f"Host: {self.host}, User: {self.user}, Password: {self.password}, Settings: {self.settings}"
