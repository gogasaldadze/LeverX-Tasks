from .base import BaseAnalysis


# Smallest average age by room
class SmallestAverageAge(BaseAnalysis):

    def run(self):

        query = """
                SELECT r.id, r.name, AVG(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS AVG_AGE
                FROM rooms r
                join students s
                    ON s.room_id = r.id
                GROUP BY r.id, r.name
                ORDER BY AVG_AGE
                LIMIT 5;               
                """

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
