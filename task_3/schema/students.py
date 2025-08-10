from .base import BaseSchema

import mysql.connector


class StudentSchema(BaseSchema):

    def create(self):
        self.cursor.execute("DROP TABLE IF EXISTS students")
        self.cursor.execute(
            """                 
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            birthday DATE NOT NULL,
            sex ENUM('M', 'F') NOT NULL,
            room_id INT,
            FOREIGN KEY (room_id) REFERENCES rooms(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
                            )
                            """
        )
        self.connection.commit()
