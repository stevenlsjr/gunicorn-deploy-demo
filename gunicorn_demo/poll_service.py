import psycopg2


class PollService():
    def __init__(self, db):
        self.db = db

    def list(self, limit=0, offset=50):
        polls = []

        with self.db.cursor() as cursor:
            cursor.execute(
                """
            SELECT 
                id,
                name,
                description,
                agree_count,
                disagree_count FROM poll
            LIMIT %s
            OFFSET %s
            """, (limit, offset))
            for row in cursor:
                polls.append(self.serialize_poll(row))
        return polls

    def get(self, id):
        with self.db.cursor() as cursor:
            cursor.execute(
                """
            SELECT 
                id,
                name,
                description,
                agree_count,
                disagree_count FROM poll
            WHERE id = %s
            """, (id,))
            return self.serialize_poll(cursor.fetchone())
            

    def serialize_poll(self, poll):
        return {
            'id': poll['id'],
            'name': poll['name'],
            'description': poll['description'],
            'agree_count': poll['agree_count'],
            'disagree_count': poll['disagree_count'],
        }
