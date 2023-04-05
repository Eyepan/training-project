from flask import Flask, render_template
from database import DB


app = Flask(__name__)
my_db = DB()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/students")
def show_students():
    students = my_db.run_query("SELECT * FROM students")
    return render_template("students.html", students=students)


if __name__ == "__main__":
    app.run()
