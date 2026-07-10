# Add simple session-based authentication to your student registry — only logged-in users can add or delete students. Non-logged-in users see the list but can't modify it. Login with hardcoded credentials. Logout button in the nav.

from flask import Flask, render_template, session, redirect, jsonify, request, flash, url_for
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from functools import wraps

app = Flask(__name__)
app.secret_key = "Secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studentsQ70.db"
db = SQLAlchemy(app)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please sign in first to perform this action.")
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper

@app.route("/login", methods = ["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("students"))
    
    if request.method == "POST":
        name = "Akash"
        passw = "0000@124"
        username = request.form["username"]
        password = request.form["password"]

        if not username:
            flash("Name cannot be empty")
        elif not password:
            flash("Password cannot be empty")
        else: 
            if len(password) >= 8:
                if username == name and password == passw:
                    session["logged_in"] = True
                    session["username"] = username
                    flash("Logged in successfully")
                    return redirect(url_for("students"))
                else:
                    flash("Wrong Username or Password")
            else:
                flash("Password cannot be less then 8 characters")

    return render_template("login.html")

class Students(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(db.String(100), nullable = False)
    age: Mapped[int] = mapped_column(nullable = False)
    score: Mapped[float] = mapped_column(nullable = False)

with app.app_context():
    db.create_all()

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
    
    return render_template("homeQ70.html", studentList = studentList)

@app.route("/student/<int:id>")
def student_profile(id):
    student = db.session.get(Students, id)
    if student is None:
        flash("Student not found")
        return redirect(url_for("students"))
    return render_template("infoQ70.html", student = student)

@app.route("/addStudent", methods=["GET", "POST"])
@login_required
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

    return render_template("addStudentQ70.html")  

@app.route("/delete/<int:id>", methods = ["POST"])
@login_required
def delStudent(id):
    student = db.session.get(Students, id)
    if student is None:
        flash("Student not found")
        return redirect(url_for("students"))
    db.session.delete(student)
    db.session.commit()
    flash("Student Data Deleted Successfully")
    return redirect(url_for("students"))

@app.route("/logout", methods = ["POST"])
def logout():
    session.clear()
    flash("Logged out")
    return redirect(url_for("students"))

app.run(debug = True)