from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (just a Python list)
tasks = [
    {"id": 1, "task": "Learn Python", "done": False},
    {"id": 2, "task": "Build REST API", "done": False}
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# GET single task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((t for t in tasks if t["id"] == id), None)
    if task:
        return jsonify(task)
    return jsonify({"message": "Task not found"}), 404

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    tasks.append(task)
    return jsonify(task), 201

# PUT to update a task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    data = request.get_json()
    task.update(data)
    return jsonify(task)

# DELETE a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
