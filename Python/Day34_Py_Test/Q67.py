# Add user authentication to your Flask app. Create a `login` route that accepts username and password (hardcode valid credentials for now), stores user info in the session on success, and redirects to a protected dashboard page. The dashboard route should redirect to login if no session exists.

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        name = "Akash"
        passw = "0000@124"
        username = request.form["username"]
        password = request.form["password"]
        session["logged_in"] = False

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
                    return redirect(url_for("dashboard"))
                else:
                    flash("Wrong Username or Password")
            else:
                flash("Password cannot be less then 8 characters")

    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    if session.get("logged_in"):
        return render_template("dashboardQ67.html")
    else:
        return redirect(url_for("home"))

app.run(debug = True)