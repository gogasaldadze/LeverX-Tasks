from .base import BaseSchema


class RoomTable(BaseSchema):

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rooms (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE
            )
        """
        )
