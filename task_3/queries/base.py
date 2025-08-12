from abc import ABC, abstractmethod


class BaseSchema(ABC):

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor(dictionary=True)

    @abstractmethod
    def count_students_in_room(self):
        pass

    @abstractmethod
    def largest_age_differecne(self):
        pass

    @abstractmethod
    def smallest_average_age(self):
        pass

    @abstractmethod
    def students_different_sex(self):

        pass
