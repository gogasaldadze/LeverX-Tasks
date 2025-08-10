from .base import BaseSchema


class RoomSchema(BaseSchema):

    def create(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS rooms (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """
        )
        self.connection.commit()
