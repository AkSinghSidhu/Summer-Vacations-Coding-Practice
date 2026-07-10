# Build a complete Flask "student registry" app: a homepage listing all students from a SQLite database, a form to add a new student (name, age, score — all validated), a page showing one student's details, and a delete button. Full CRUD, database-backed, with flash messages for feedback.

from flask import Flask, render_template, session, redirect, jsonify, request, flash, url_for
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.secret_key = "Secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db = SQLAlchemy(app)

class Students(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(db.String(100), nullable = False)
    age: Mapped[int] = mapped_column(nullable = False)
    score: Mapped[float] = mapped_column(nullable = False)

with app.app_context():
    db.create_all()

@app.route("/addStudent", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        score = request.form["score"]
        if not name:
            flash("Name cannot be empty")
        elif not age:
            flash("Age cannot be empty")
        elif not score:
            flash("Score cannot be empty")
        else:
            try:
                age_int = int(age)
                if 1 <= age_int <= 120:
                    try:
                        score_float = float(score)
                        if 0 <= score_float <= 100:
                            user = Students(name = name, age = age_int, score = score_float)
                            db.session.add(user)
                            db.session.commit()
                            flash("User Added")
                        else:
                            flash("Invalid Score! Score cannot be negative or more than 100.")
                    except ValueError:
                        flash("Score must be a number.")
                else:
                    flash("Invalid Age! Age cannot be Negative or more than 120.")
            except ValueError:
                flash("Age must be a number.")

    return render_template("addStudent.html")  

@app.route("/")
def students():
    studentList = []
    students = db.session.scalars(
        select(Students)
    ).all()
    for student in students:
        studentList.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "score": student.score
        })
    
    return render_template("home.html", studentList = studentList)

@app.route("/student/<int:id>")
def student_profile(id):
    student = db.session.get(Students, id)
    if student is None:
        flash("Student not found")
        return redirect(url_for("students"))
    return render_template("info.html", student = student)

@app.route("/delete/<int:id>", methods = ["POST"])
def delStudent(id):
    student = db.session.get(Students, id)
    if student is None:
        flash("Student not found")
        return redirect(url_for("students"))
    db.session.delete(student)
    db.session.commit()
    flash("Student Data Deleted Successfully")
    return redirect(url_for("students"))

app.run(debug = True)