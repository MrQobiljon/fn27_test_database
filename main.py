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

    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            course_name VARCHAR(10)
        );'''
        self.manager(sql, commit=True)

    def create_table_students(self):
        sql = '''CREATE TABLE IF NOT EXISTS students(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            course_id INTEGER REFERENCES courses(id)
        );'''
        self.manager(sql, commit=True)
