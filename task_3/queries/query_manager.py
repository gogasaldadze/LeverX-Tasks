from .base import BaseSchema


class QueryManager(BaseSchema):

    def count_students_in_room(self):
        query = """
                SELECT r.id, r.name, COUNT(s.name) as student_quantity
                FROM rooms r
                JOIN students s ON s.room_id = r.id
                GROUP BY r.id, r.name
        
                """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def largest_age_differecne(self):
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

    def smallest_average_age(self):
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

    def students_different_sex(self):
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
