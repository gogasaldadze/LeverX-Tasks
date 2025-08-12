from abc import ABC, abstractmethod


class BaseSchema(ABC):

    @abstractmethod
    def load_students(self):
        pass

    @abstractmethod
    def load_rooms(self):
        pass
