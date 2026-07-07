# Add a form to your Flask app that accepts a name and age. On submit, validate that name is not empty and age is a number between 1 and 120. If valid, redirect to a results page showing the submitted data. If invalid, show the form again with an error message.

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        logged_in = "Logged in successfully"

        if not username:
            error = "Name cannot be empty"
        elif not age:
            error = "Age cannot be empty"
        else:
            try:
                age_int = int(age)
                if 1 <= age_int <= 120:
                    session["username"] = username
                    session["age"] = age
                    session["logged_in"] = logged_in
                    return redirect(url_for("profile"))
                else:
                    error = "Age must be between 1 and 120"
            except ValueError:
                error = "Age must be a number"

    return render_template("formQ63.html", error = error)

@app.route("/profile")
def profile():
    return render_template("profileQ63.html")

app.run(debug = True)