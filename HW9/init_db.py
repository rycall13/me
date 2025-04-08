import sqlite3
import os

# Make sure the data folder exists
os.makedirs('data', exist_ok=True)

def init_db():
    conn = sqlite3.connect('data/school.db')
    c = conn.cursor()

    # Create students table
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            year TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    # Create teachers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    # Create classes table
    c.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT DEFAULT 'Misc',
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')

    # Create schools table
    c.execute('''
        CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized ✅")
