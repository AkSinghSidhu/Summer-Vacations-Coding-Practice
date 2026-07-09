# Add a logout route that clears the session. Add a `login_required` decorator (write it yourself, don't use Flask-Login library) that checks for a session and redirects to login if missing. Apply it to the dashboard route.

from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("home"))
        return func(*args, **kwargs)
    
    return wrapper

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
@login_required
def dashboard():
    return render_template("dashboardQ68.html")
    
@app.route("/logout", methods = ["POST"])
def logout():
    session.clear()
    flash("Logged out")
    return redirect(url_for("home"))


app.run(debug = True)