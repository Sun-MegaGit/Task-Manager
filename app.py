from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        tasks.append({'task_name': task_name, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['GET'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_index>', methods=['GET'])
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
