from collections import defaultdict
from .models import Room, Student


class Merger:
    @staticmethod
    def merge(students, rooms):

        # group students by their rooms with using defualtdict to avoid extra coding for appending
        result = defaultdict(list)
        for student in students:
            result[student.room].append(student)

        # adding students to dedicated room.
        return [
            Room(id=room["id"], name=room["name"], students=result[room["id"]])
            for room in rooms
        ]
