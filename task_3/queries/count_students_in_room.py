from .base import BaseAnalysis


class CountStudentsInRoom(BaseAnalysis):

    def run(self):
        query = """
                SELECT r.id, r.name, COUNT(s.name) as student_quantity
                FROM rooms r
                JOIN students s ON s.room_id = r.id
                GROUP BY r.id, r.name
        
                """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
