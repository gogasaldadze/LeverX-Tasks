from .base import BaseSchema


class IndexManager(BaseSchema):
    def create(self):
        # index on students.room_id
        self.cursor.execute("CREATE INDEX idx_students_room_id ON students(room_id);")

        # index on students.birthday
        self.cursor.execute("CREATE INDEX idx_students_birthday ON students(birthday)")

        print("Indexes Created Successfully : students.room_id, students.birthday ")
        self.connection.commit()
