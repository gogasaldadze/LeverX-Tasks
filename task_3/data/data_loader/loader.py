from .base import BaseSchema
import json


class DataLoader(BaseSchema):
    def load_rooms(self):

        with open("data/rooms.json", "r") as f:
            rooms = json.load(f)

        return rooms

    def load_students(self):
        with open("data/students.json", "r") as f:
            students = json.load(f)

        return students
