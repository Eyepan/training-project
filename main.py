from flask import Flask
from database import DB


app = Flask(__name__)
my_db = DB()


@app.route("/")
def index():
    return "hi there"


@app.route("/students")
def show_students():
    return my_db.run_query("SELECT * FROM students")


if __name__ == "__main__":
    app.run()
