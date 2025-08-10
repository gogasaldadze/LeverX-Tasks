from .base import BaseInserter


class RoomInserter(BaseInserter):

    def insert(self, rooms):
        insert_query = """
        INSERT INTO rooms (id, name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name)
        """

        data = [(room["id"], room["name"]) for room in rooms]

        self.cursor.executemany(insert_query, data)
        self.connection.commit()
