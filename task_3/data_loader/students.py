from .base import BaseDataLoader
import json


class StudentDataLoader(BaseDataLoader):

    def load(self):
        with open("data/students.json", "r") as f:
            students = json.load(f)

        return students
