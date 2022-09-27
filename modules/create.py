class Create:
    def __init__(self, cursor, table, columns, values):
        self.table = table
        self.columns = columns
        self.values = values
        self.cursor = cursor
    def create(self, cursor, table, columns, values):
        self.cursor = cursor
        self.cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)})")