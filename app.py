from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
todos = []
_next_id = 1


@app.get("/api/todos")
def list_todos():
    return jsonify(todos)


@app.post("/api/todos")
def add_todo():
    global _next_id
    data = request.get_json(force=True)
    todo = {"id": _next_id, "title": data["title"], "done": False}
    todos.append(todo)
    _next_id += 1
    return jsonify(todo), 201


@app.get("/")
def index():
    return render_template("index.html", todos=todos)
