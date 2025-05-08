import sqlite3
import csv

def import_trainers(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO trainer (name, email, phone)
                VALUES (?, ?, ?)
            ''', (row['name'], row['email'], row['phone']))
    
    conn.commit()
    conn.close()