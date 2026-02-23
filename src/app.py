from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database config from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/postgres"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return "Secure-CRUD is running!"

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    task.title = request.json["title"]
    db.session.commit()
    return jsonify({"message": "Updated"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)