import sqlite3


class DB:
    def __init__(self):
        self.run_query(
            """CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                mail TEXT NOT NULL,
                phone TEXT NOT NULL,
                dob DATETIME NOT NULL,
                gender TEXT NOT NULL,
                address_1 TEXT NOT NULL,
                address_2 TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL, 
                zip TEXT NOT NULL,
                country TEXT NOT NULL
            )""")

    def run_query(self, query: str, **kwargs):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(query, kwargs)
        conn.commit()
        result = c.fetchall()
        conn.close()
        return result
