import sqlite3
import csv

def import_teams(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO team (name, manager_id)
                VALUES (?, ?)
            ''', (row['name'], row['manager_id']))
    
    conn.commit()
    conn.close()