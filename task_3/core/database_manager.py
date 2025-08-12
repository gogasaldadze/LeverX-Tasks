from mysql.connector import connect, Error


class DBManager:
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

    def create_database(self, database_name):
        connection = self.get_connection()
        if not connection:
            print("Connection Failed")
            return False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
                result = cursor.fetchone()
                if not result:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
                    print(f"Database successfully created: {database_name}")
                else:
                    print(f"Database already exists: {database_name}")
            connection.close()
            return True
        except Error as e:
            print("Error occurred while creating database:", e)
            return False
