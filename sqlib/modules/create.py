from sqlib.modules.connection import *

class Create:
    def create(self, cursor, table, columns, values):
        cursor.execute(query=f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)})")
