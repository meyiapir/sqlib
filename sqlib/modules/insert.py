
class Insert:
    def insert(self, cursor, table: str, columns: str | list, values: str | int | list) -> None:
        """
        It takes a cursor, a table name, a list of columns, and a list of values, and inserts the values into the table.

        :param cursor:
        :param table: The table name
        :param columns: a list of column names
        :param values: a list of values to insert into the table
        """
        vals = ''
        for val in values:
            vals += f"'{val}', "
        vals = vals[:-2]
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({vals})"
        print(query)
        cursor.execute(query=query)
