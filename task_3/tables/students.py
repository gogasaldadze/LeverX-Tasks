from .base import BaseSchema


class StudentTable(BaseSchema):

    def create_table(self):
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    birthday DATE NOT NULL,
                    sex ENUM('M', 'F') NOT NULL,
                    room_id INT DEFAULT NULL,
                    FOREIGN KEY (room_id) REFERENCES rooms(id)
                        ON DELETE SET NULL
                        ON UPDATE CASCADE
                )
            """
        )

    def create_indexes(self):
        self.cursor.execute("CREATE INDEX idx_students_room_id ON students(room_id);")
        self.cursor.execute("CREATE INDEX idx_students_birthday ON students(birthday)")

        print("Indexes Created successfully : students.room_id, students.birthday ")
