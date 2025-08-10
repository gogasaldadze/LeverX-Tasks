from .base import BaseAnalysis


class LargestAgeDifference(BaseAnalysis):

    def run(self):
        query = """
                SELECT r.id, r.name, MAX(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS MAX_AGE,
                MIN(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS MIN_AGE,
                MAX(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) - MIN(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS MAX_AGE_DIFFERENCE
                FROM rooms r
                JOIN students s 
                    ON s.room_id = r.id
                GROUP BY r.id, r.name
                ORDER BY MAX_AGE_DIFFERENCE DESC
                LIMIT 5;
                            
                """

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
