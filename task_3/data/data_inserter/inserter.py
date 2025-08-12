from .base import BaseSchema
from datetime import datetime


class DataInserter(BaseSchema):

    def insert_students_data(self, students):

        insert_query = """
        INSERT INTO students (id, name, birthday, sex, room_id)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            birthday = VALUES(birthday),
            sex = VALUES(sex),
            room_id = VALUES(room_id)
        """
        data = []
        for student in students:
            birthday_date = datetime.fromisoformat(student["birthday"]).date()
            data.append(
                (
                    student["id"],
                    student["name"],
                    birthday_date,
                    student["sex"],
                    student["room"],
                )
            )
        self.cursor.executemany(insert_query, data)
        self.connection.commit()

    def insert_rooms_data(self, rooms):

        insert_query = """
        INSERT INTO rooms (id, name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name)
        """

        data = [(room["id"], room["name"]) for room in rooms]

        self.cursor.executemany(insert_query, data)
        self.connection.commit()
