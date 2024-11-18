from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

student_name = ["Spongebob", "Jimmy Neutron", "Alice"]

@app.route('/')
def fetch_student_list():
    student_with_index = list(enumerate(student_name))
    return render_template('index.html', students=student_with_index)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    if name:
        student_name.append(name)
    return redirect(url_for('fetch_student_list'))

@app.route('/delete/<name>', methods=['POST'])
def delete_student(name):
    if name in student_name:
        student_name.remove(name)
    return redirect(url_for('fetch_student_list'))

@app.route('/delete_index/<int:index>', methods=['POST'])
def delete_student_with_index(index):
    if 0 <= index < len(student_name):
        student_name.pop(index)
    return redirect(url_for('fetch_student_list'))

@app.route('/select/<name>')
def selected_student(name):
    print("selected ", name)
    return redirect(url_for('fetch_student_list'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit_student(index):
    new_name = request.form.get("new_name")
    if 0 <= index < len(student_name) and new_name:
        student_name[index] = new_name
    return redirect(url_for('fetch_student_list'))

if __name__ == '__main__':
    app.run(debug=True)
