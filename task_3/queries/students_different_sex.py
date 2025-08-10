from .base import BaseAnalysis


class StudentDifferentSex(BaseAnalysis):

    def run(self):
        query = """
            SELECT r.id, r.name
            FROM rooms r 
            JOIN students s
                ON s.room_id = r.id
            GROUP BY r.id, r.name
            HAVING COUNT(DISTINCT s.sex) > 1;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
