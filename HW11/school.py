from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(__name__)
DB_PATH = 'data/school.db'

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def check_required_fields(data, fields):
    for field in fields:
        if field not in data or not data[field]:
            return {'error': f'{field} is required'}, 500
    return None

@app.route('/student', methods=['GET', 'POST', 'DELETE'])
def student():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        required = ['name', 'email', 'phone', 'year', 'status']
        error = check_required_fields(data, required)
        if error:
            return error

        c.execute('INSERT INTO students (name, email, phone, year, status) VALUES (?, ?, ?, ?, ?)',
                  (data['name'], data['email'], data['phone'], data['year'], data['status']))
        conn.commit()
        new_id = c.lastrowid
        return jsonify({'id': new_id})

    elif request.method == 'GET':
        student_id = request.args.get('id')
        if not student_id:
            return {'error': 'id is required'}, 500
        c.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = c.fetchone()
        if student:
            return jsonify(dict(student))
        else:
            return {'error': 'Student not found'}, 404

    elif request.method == 'DELETE':
        data = request.get_json()
        if not data or 'id' not in data:
            return {'error': 'id is required'}, 500
        c.execute('DELETE FROM students WHERE id = ?', (data['id'],))
        conn.commit()
        return jsonify({'message': 'Student deleted'})

@app.route('/teacher', methods=['GET', 'POST', 'DELETE'])
def teacher():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        required = ['name', 'email', 'phone']
        error = check_required_fields(data, required)
        if error:
            return error

        c.execute('INSERT INTO teachers (name, email, phone) VALUES (?, ?, ?)',
                  (data['name'], data['email'], data['phone']))
        conn.commit()
        new_id = c.lastrowid
        return jsonify({'id': new_id})

    elif request.method == 'GET':
        teacher_id = request.args.get('id')
        count = request.args.get('count')

        if not teacher_id:
            return {'error': 'id is required'}, 500

        c.execute('SELECT * FROM teachers WHERE id = ?', (teacher_id,))
        teacher = c.fetchone()

        if teacher:
            teacher_data = dict(teacher)
            if count == 'true':
                c.execute('SELECT COUNT(*) FROM classes WHERE teacher_id = ?', (teacher_id,))
                classes_count = c.fetchone()[0]
                teacher_data['count'] = classes_count
            return jsonify(teacher_data)
        else:
            return {'error': 'Teacher not found'}, 404

    elif request.method == 'DELETE':
        data = request.get_json()
        if not data or 'id' not in data:
            return {'error': 'id is required'}, 500
        c.execute('DELETE FROM teachers WHERE id = ?', (data['id'],))
        conn.commit()
        return jsonify({'message': 'Teacher deleted'})

@app.route('/class', methods=['GET', 'POST', 'DELETE'])
def class_():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        required = ['name']
        error = check_required_fields(data, required)
        if error:
            return error

        department = data.get('department', 'Misc')
        teacher_id = data.get('teacher_id')

        c.execute('INSERT INTO classes (name, department, teacher_id) VALUES (?, ?, ?)',
                  (data['name'], department, teacher_id))
        conn.commit()
        new_id = c.lastrowid
        return jsonify({'id': new_id})

    elif request.method == 'GET':
        class_id = request.args.get('id')
        count = request.args.get('count')

        if count == 'true':
            c.execute('SELECT COUNT(*) FROM classes')
            class_count = c.fetchone()[0]
            return jsonify({'count': class_count})

        if not class_id:
            return {'error': 'id is required'}, 500

        c.execute('SELECT * FROM classes WHERE id = ?', (class_id,))
        class_data = c.fetchone()
        if class_data:
            return jsonify(dict(class_data))
        else:
            return {'error': 'Class not found'}, 404

    elif request.method == 'DELETE':
        class_id = request.args.get('id')
        if not class_id:
            return {'error': 'id is required'}, 500
        c.execute('DELETE FROM classes WHERE id = ?', (class_id,))
        conn.commit()
        return jsonify({'message': 'Class deleted'})

@app.route('/student/update_phone', methods=['POST'])
def update_student_phone():
    conn = get_db_connection()
    c = conn.cursor()
    student_id = request.args.get('id')
    phone = request.args.get('phone')
    if not student_id or not phone:
        return {'error': 'id and phone are required'}, 500

    c.execute('UPDATE students SET phone = ? WHERE id = ?', (phone, student_id))
    conn.commit()
    return jsonify({'message': 'Student phone updated'})

@app.route('/teacher/update_phone', methods=['POST'])
def update_teacher_phone():
    conn = get_db_connection()
    c = conn.cursor()
    teacher_id = request.args.get('id')
    phone = request.args.get('phone')
    if not teacher_id or not phone:
        return {'error': 'id and phone are required'}, 500

    c.execute('UPDATE teachers SET phone = ? WHERE id = ?', (phone, teacher_id))
    conn.commit()
    return jsonify({'message': 'Teacher phone updated'})

@app.route('/department', methods=['POST', 'DELETE'])
def department():
    conn = get_db_connection()
    c = conn.cursor()
    data = request.get_json()

    if request.method == 'POST':
        required = ['id', 'name', 'school_id']
        error = check_required_fields(data, required)
        if error:
            logging.error(f"Missing required field(s) for department creation: {data}")
            return error

        c.execute('SELECT * FROM schools WHERE id = ?', (data['school_id'],))
        school = c.fetchone()
        if not school:
            logging.error(f"Attempted to create department with invalid school_id {data['school_id']}")
            return {'error': 'Invalid school_id'}, 400

        c.execute('INSERT INTO departments (id, name, school_id) VALUES (?, ?, ?)',
                  (data['id'], data['name'], data['school_id']))
        conn.commit()
        logging.debug(f"Created department: {data}")
        return jsonify({'message': 'Department created'})

    elif request.method == 'DELETE':
        if 'id' not in data:
            logging.error("Missing department id for deletion")
            return {'error': 'id is required'}, 500
        c.execute('DELETE FROM departments WHERE id = ?', (data['id'],))
        conn.commit()
        logging.debug(f"Deleted department ID: {data['id']}")
        return jsonify({'message': 'Department deleted'})

@app.route('/course', methods=['POST', 'DELETE'])
def course():
    conn = get_db_connection()
    c = conn.cursor()
    data = request.get_json()

    if request.method == 'POST':
        required = ['id', 'name', 'dept_id']
        error = check_required_fields(data, required)
        if error:
            logging.error(f"Missing required field(s) for course creation: {data}")
            return error

        c.execute('SELECT * FROM departments WHERE id = ?', (data['dept_id'],))
        dept = c.fetchone()
        if not dept:
            logging.error(f"Attempted to create course with invalid dept_id {data['dept_id']}")
            return {'error': 'Invalid dept_id'}, 400

        c.execute('INSERT INTO courses (id, name, dept_id) VALUES (?, ?, ?)',
                  (data['id'], data['name'], data['dept_id']))
        conn.commit()
        logging.debug(f"Created course: {data}")
        return jsonify({'message': 'Course created'})

    elif request.method == 'DELETE':
        if 'id' not in data:
            logging.error("Missing course id for deletion")
            return {'error': 'id is required'}, 500
        c.execute('DELETE FROM courses WHERE id = ?', (data['id'],))
        conn.commit()
        logging.debug(f"Deleted course ID: {data['id']}")
        return jsonify({'message': 'Course deleted'})

if __name__ == '__main__':
    app.run(debug=False)
