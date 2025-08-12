from abc import ABC, abstractmethod


class BaseSchema(ABC):
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    @abstractmethod
    def insert_rooms_data(self, rooms):
        pass

    @abstractmethod
    def insert_students_data(self, students):

        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
