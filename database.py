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
        if self.run_query("select * from students") is None:
            self.run_query("INSERT INTO students(first_name, last_name, mail, phone, dob, gender, address_1, address_2, city, state, zip, country) VALUES(:f, :l, :m, :p, :d, :g, :a1, :a2, :c, :s, :z, :co)",
                           f="Bob", l="Reacher", m="dummy@mail.com", p="7904377168", d="14-09-2002", g="M", a1="1234", a2="5678", c="New York", s="New York", z="12345", co="USA")

    def run_query(self, query: str, **kwargs):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(query, kwargs)
        conn.commit()
        result = c.fetchall()
        conn.close()
        return result
