import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='education',
            user='postgres',
            host='localhost',
            password='123456'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result
