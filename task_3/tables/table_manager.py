from .students import StudentTable
from .rooms import RoomTable


class TableManager:
    def __init__(self, connection):
        self.connection = connection
        self.room_table = RoomTable(connection)
        self.student_table = StudentTable(connection)

    def __enter__(self):
        return self

    def create_all(self):
        # create tables
        self.room_table.create_table()
        self.student_table.create_table()

        # create indexes
        self.student_table.create_indexes()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
