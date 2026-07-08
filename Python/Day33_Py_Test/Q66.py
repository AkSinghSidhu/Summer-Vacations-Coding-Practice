# Add routes for: fetching a single user by id (404 if not found), updating a user's name, and deleting a user. Test all routes — you now have a full CRUD API backed by a real database.

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

@app.route("/users/<int:id>", methods = ["GET"])
def search_user(id):
    user = db.session.get(User, id)
    if user:
        return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": str(user.created_at)
    })
    else:
        return "User not found", 404

@app.route("/users/<int:id>", methods = ["PATCH"])
def update_name(id):
    user = db.session.get(User, id)
    if user:
        user.name = "Supan"
        db.session.commit()
        return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": str(user.created_at)
    })
    else:
        return "User not found", 404

@app.route("/users/<int:id>", methods = ["DELETE"])
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User deleted", 200
    else:
        return "User not found", 404

app.run(debug = True)