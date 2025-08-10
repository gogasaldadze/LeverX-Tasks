from .base import BaseInserter
from datetime import datetime


class StudentInserter(BaseInserter):

    def insert(self, students):
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
