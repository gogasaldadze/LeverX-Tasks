from .base import BaseSchema


class TableManager(BaseSchema):
    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS students")
        self.cursor.execute("DROP TABLE IF EXISTS rooms")

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rooms (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE
            )
        """
        )

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

        self.connection.commit()

    def create_indexes(self):

        # index on students.room_id
        self.cursor.execute("CREATE INDEX idx_students_room_id ON students(room_id);")

        # index on students.birthday
        self.cursor.execute("CREATE INDEX idx_students_birthday ON students(birthday)")

        print("Indexes Created Successfully : students.room_id, students.birthday ")
        self.connection.commit()

    def create_all(self):

        self.create_table()
        self.create_indexes()
