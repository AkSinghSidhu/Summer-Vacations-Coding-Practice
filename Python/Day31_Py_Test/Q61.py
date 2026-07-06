# Set up a basic Flask app with three routes: `/` returns a homepage, `/about` returns an about page, `/user/<name>` returns a personalised greeting using the URL parameter. Run it and test all routes in the browser.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/user/<name>")
def user(name):
    return f"Hi {name}"

app.run(debug = True)