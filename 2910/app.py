from flask import Flask, jsonify, request
from db_utils import get_completed_tasks, add_task

app = Flask(__name__)

@app.route('/completed')
def completed_tasks():
    result = get_completed_tasks()
    return jsonify(result)


@app.route('/add', methods=['PUT'])    
def add():
    task = request.get_json()
    add_task()
    return task

if __name__ == '__main__':
    app.run(debug=True, port=5001)