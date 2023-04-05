from flask import Flask, redirect, render_template, request
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


@app.route("/students", methods=['POST'])
def add_student():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    mail = request.form.get("mail")
    phone = request.form.get("phone")
    dob = request.form.get("dob")
    gender = request.form.get("gender")
    address_1 = request.form.get("address_1")
    address_2 = request.form.get("address_2")
    city = request.form.get("city")
    state = request.form.get("state")
    zip = request.form.get("zip")
    country = request.form.get("country")

    l = len(my_db.run_query("SELECT * FROM students"))
    my_db.run_query("INSERT INTO students VALUES (:id, :f, :l, :m, :p, :d, :g, :a1, :a2, :c, :s, :z, :co)",
                    id=l, f=first_name, l=last_name, m=mail, p=phone, d=dob, g=gender, a1=address_1, a2=address_2, c=city, s=state, z=zip, co=country)
    return redirect("/students")


@app.route("/create")
def create():
    return render_template("addstudent.html")


if __name__ == "__main__":
    app.run()
