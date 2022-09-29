import mariadb


class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cursor = None
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            return self.cursor
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            exit(1)

    def execute(self, *, query, watch_mode=0):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            if watch_mode == 1:
                return self.cursor.fetchall()
        except mariadb.Error as e:
            print(f"Error executing query: {e}")
            exit(1)

    def close(self):
        self.conn.close()
