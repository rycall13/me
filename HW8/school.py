from flask import Flask, request, jsonify
import os
import pandas as pd

app = Flask(__name__)

DATA_DIR = 'data'
STUDENT_FILE = os.path.join(DATA_DIR, 'student.csv')
TEACHER_FILE = os.path.join(DATA_DIR, 'teacher.csv')
CLASS_FILE = os.path.join(DATA_DIR, 'class.csv')

os.makedirs(DATA_DIR, exist_ok=True)

for file, columns in [
    (STUDENT_FILE, ['ID', 'Name', 'Email', 'Phone', 'Year', 'Status']),
    (TEACHER_FILE, ['ID', 'Name', 'Email', 'Phone']),
    (CLASS_FILE, ['ID', 'Name', 'Department', 'TeacherID'])
]:
    if not os.path.exists(file):
        pd.DataFrame(columns=columns).to_csv(file, index=False)

def load_csv(file):
    return pd.read_csv(file)

def save_csv(df, file):
    df.to_csv(file, index=False)

def missing_fields(data, required_fields):
    for field in required_fields:
        if field not in data:
            return field
    return None

@app.route('/student', methods=['GET', 'POST', 'DELETE'])
def student():
    if request.method == 'POST':
        data = request.json
        required = ['ID', 'Name', 'Email', 'Phone', 'Year', 'Status']
        missing = missing_fields(data, required)
        if missing:
            return jsonify({'error': f'{missing} is required'}), 500
        df = load_csv(STUDENT_FILE)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        save_csv(df, STUDENT_FILE)
        return jsonify({'message': 'Student added'}), 201

    elif request.method == 'DELETE':
        data = request.json
        if 'id' not in data:
            return jsonify({'error': 'id is required'}), 500
        df = load_csv(STUDENT_FILE)
        df = df[df['ID'] != data['id']]
        save_csv(df, STUDENT_FILE)
        return jsonify({'message': 'Student deleted'}), 200

    elif request.method == 'GET':
        student_id = request.args.get('id')
        if not student_id:
            return jsonify({'error': 'id is required'}), 500
        df = load_csv(STUDENT_FILE)
        student_data = df[df['ID'] == student_id]
        if student_data.empty:
            return jsonify({'error': 'Student not found'}), 404
        return jsonify(student_data.iloc[0].to_dict())

@app.route('/teacher', methods=['GET', 'POST', 'DELETE'])
def teacher():
    if request.method == 'POST':
        data = request.json
        required = ['ID', 'Name', 'Email', 'Phone']
        missing = missing_fields(data, required)
        if missing:
            return jsonify({'error': f'{missing} is required'}), 500
        df = load_csv(TEACHER_FILE)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        save_csv(df, TEACHER_FILE)
        return jsonify({'message': 'Teacher added'}), 201

    elif request.method == 'DELETE':
        data = request.json
        if 'id' not in data:
            return jsonify({'error': 'id is required'}), 500
        df = load_csv(TEACHER_FILE)
        df = df[df['ID'] != data['id']]
        save_csv(df, TEACHER_FILE)
        return jsonify({'message': 'Teacher deleted'}), 200

    elif request.method == 'GET':
        teacher_id = request.args.get('id')
        df = load_csv(TEACHER_FILE)
        teacher_data = df[df['ID'] == teacher_id]
        if teacher_data.empty:
            return jsonify({'error': 'Teacher not found'}), 404
        result = teacher_data.iloc[0].to_dict()

        if request.args.get('count') == 'true':
            class_df = load_csv(CLASS_FILE)
            result['count'] = class_df[class_df['TeacherID'] == teacher_id].shape[0]

        return jsonify(result)

@app.route('/class', methods=['GET', 'POST', 'DELETE'])
def class_endpoint():
    if request.method == 'POST':
        data = request.json
        required = ['ID', 'Name', 'TeacherID']
        missing = missing_fields(data, required)
        if missing:
            return jsonify({'error': f'{missing} is required'}), 500
        data.setdefault('Department', 'Misc')
        df = load_csv(CLASS_FILE)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        save_csv(df, CLASS_FILE)
        return jsonify({'message': 'Class added'}), 201

    elif request.method == 'DELETE':
        class_id = request.args.get('id')
        if not class_id:
            return jsonify({'error': 'id is required'}), 500
        df = load_csv(CLASS_FILE)
        df = df[df['ID'] != class_id]
        save_csv(df, CLASS_FILE)
        return jsonify({'message': 'Class deleted'}), 200

    elif request.method == 'GET':
        if request.args.get('count') == 'true':
            df = load_csv(CLASS_FILE)
            return jsonify({'count': df.shape[0]})
        class_id = request.args.get('id')
        if not class_id:
            return jsonify({'error': 'id is required'}), 500
        df = load_csv(CLASS_FILE)
        class_data = df[df['ID'] == class_id]
        if class_data.empty:
            return jsonify({'error': 'Class not found'}), 404
        return jsonify(class_data.iloc[0].to_dict())

if __name__ == '__main__':
    app.run(debug=False)
