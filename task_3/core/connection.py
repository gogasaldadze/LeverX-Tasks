from mysql.connector import connect, Error


class ConnectionManager:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def get_connection(self):
        try:
            return connect(host=self.host, user=self.user, password=self.password)
        except Error as e:
            print("Connection failed:", e)
            return None

    def get_connection_with_db(self, database):
        try:
            return connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database,
            )
        except Error as e:
            print(f"Connection to database '{database}' failed:", e)
            return None
