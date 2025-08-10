from mysql.connector import Error


class CreateDataBase:
    def __init__(self, raw_connection, name):
        self.connection = raw_connection
        self.name = name

    def create(self):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("SHOW DATABASES LIKE %s", (self.name,))
                    result = cursor.fetchone()
                    if not result:
                        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.name}")
                        print(f"Database successfully created: {self.name}")
                    else:
                        print(f"Database already exists: {self.name}")
            except Error as e:
                print("Error occurred while creating database:", e)
        else:
            print("Connection Failed")
