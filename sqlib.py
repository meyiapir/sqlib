from modules.connection import *
from modules.select import *
from loguru import logger

class Sqlib(Connection, Select):
    def __init__(self, host: str, user: str, password: str, settings: dict):
        super().__init__(host, user, password, settings["database"])
        self.host = host
        self.user = user
        self.password = password
        self.settings = settings

    def select(self, table: str, columns: list, where: dict = None, limit: int = None):
        return super().select(table, columns, where, limit)

    def __str__(self) -> str:
        return f"Host: {self.host}, User: {self.user}, Password: {self.password}, Settings: {self.settings}"
