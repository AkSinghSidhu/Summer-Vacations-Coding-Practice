# Create a simple Jinja2 template for the homepage. Pass a list of 5 items from the route to the template and render them as an HTML list using a `{% for %}` loop. Add a conditional `{% if %}` that shows a different message when the list is empty.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage"

@app.route("/user/<name>")
def user(name):
    course = "Btech"
    uid = "237106002"
    currentSubjects = ["Deep Learning", "Dev Ops", "Reinforcement Learning", "Cloud Computing", "Communication Skills"]

    return render_template(
        "info.html",
        username = name,
        uid = uid,
        course = course,
        subjects = currentSubjects
    )

app.run(debug = True)