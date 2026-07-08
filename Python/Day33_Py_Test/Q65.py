# Set up Flask-SQLAlchemy with a SQLite database. Create a `User` model with `id`, `name`, `email`, and `created_at` fields. Use `db.create_all()` to create the table. Write a route that adds a hardcoded user to the database and another that lists all users as JSON.

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.now)

with app.app_context():
    db.create_all()

@app.route("/add-user")
def add_user():
    user = User(name = "Akash", email = "aksinghsidhu07@gmail.com")
    db.session.add(user)
    db.session.commit()
    return "User added"

@app.route("/users")
def users():
    usersList = []
    users = User.query.all()
    for user in users:
        usersList.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "created_at": str(user.created_at)
        })
    
    return jsonify(usersList)

app.run(debug = True)