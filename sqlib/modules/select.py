

class Select:
    def __init__(self, cursor, table: str, columns: list, where: dict = None, limit: int = None):
        self.table = table
        self.columns = columns
        self.where = where
        self.limit = limit
        self.cursor = cursor

    def select(self, table: str, columns: list, where: dict = None, limit: int = None) -> list:

        if where is None and limit is None:
            self.cursor.execute(f"SELECT {', '.join(columns)} FROM {table}")
        elif where is None and limit is not None:
            self.cursor.execute(f"SELECT {', '.join(columns)} FROM {table} LIMIT {limit}")
        elif where is not None and limit is None:
            self.cursor.execute(
                f"SELECT {', '.join(columns)} FROM {table} WHERE {list(where.keys())[0]} = '{list(where.values())[0]}'")
        else:
            self.cursor.execute(
                f"SELECT {', '.join(columns)} FROM {table} WHERE {list(where.keys())[0]} = '{list(where.values())[0]}' LIMIT {limit}")
        return self.cursor.fetchall()

    def select_all(self, table: str, where: dict = None) -> list:
        if where is None:
            self.cursor.execute(f"SELECT * FROM {table}")
        else:
            self.cursor.execute(
                f"SELECT * FROM {table} WHERE {list(where.keys())[0]} = '{list(where.values())[0]}'")
        return self.cursor.fetchall()

    def __str__(self) -> str:
        return f"Table: {self.table}, Columns: {self.columns}, Where: {self.where}, Limit: {self.limit}"
