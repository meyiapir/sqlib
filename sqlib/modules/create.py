import json


class Create:
    def create_table(self, cursor, name: str, settings: str | dict) -> None:
        """
        Creates a table with the given name and settings.

        :param cursor: Cursor object.
        :param name: The name of the table
        :param settings: The settings of the table
        :return: None
        """

        def get_query(data) -> str:
            query = f"CREATE TABLE {name} ("
            for column in data["columns"]:
                query += f"{column} {data['columns'][column]['type']}({data['columns'][column]['length']}) "
                if data["columns"][column]["null"]:
                    query += "NULL "
                else:
                    query += "NOT NULL "
                if data["columns"][column]["default"] is not None and data["columns"][column]["default"] != "None":
                    query += f"DEFAULT {data['columns'][column]['default']} "
                if data["columns"][column]["auto_increment"]:
                    query += "AUTO_INCREMENT "
                if data["columns"][column]["primary_key"]:
                    query += "PRIMARY KEY "
                if data["columns"][column]["unique"]:
                    query += "UNIQUE "
                query += ", "
            query = query[:-2]
            query += f") ENGINE={data['engine']} " \
                     f"DEFAULT CHARSET={data['charset']} COLLATE={data['collation']} " \
                     f"AUTO_INCREMENT={data['auto_increment']} COMMENT='{data['comment']}';"
            return query

        if type(settings) == str:
            with open(settings, "r") as file:
                settings = json.load(file)
            query = get_query(settings)
        elif type(settings) == dict:
            query = get_query(settings)
        cursor.execute(query=query)
