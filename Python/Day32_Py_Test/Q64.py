# Add Flask flash messages to your form — flash a success message on valid submission and an error message on invalid input. Display them in the template using `get_flashed_messages()`.

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]

        if not username:
            flash("Name cannot be empty")
        elif not age:
            flash("Age cannot be empty")
        else: 
            try:
                age_int = int(age)
                if 1 <= age_int <= 120:
                    session["username"] = username
                    session["age"] = age
                    flash("Logged in successfully")
                    return redirect(url_for("profile"))
                else:
                    flash("Age must be between 1 and 120")
            except ValueError:
                flash("Age must be a number")

    return render_template("formQ64.html")

@app.route("/profile")
def profile():
    return render_template("profileQ64.html")

app.run(debug = True)