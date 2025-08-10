from abc import ABC, abstractmethod


class BaseAnalysis(ABC):

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor(dictionary=True)

    @abstractmethod
    def run(self):
        pass
