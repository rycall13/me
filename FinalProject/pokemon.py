import sqlite3
import csv

def import_pokemon(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
                INSERT INTO pokemon (name, height, weight, experience)
                VALUES (?, ?, ?, ?)
            ''', (row['identifier'], row['height'], row['weight'], row['base_experience']))
    
    conn.commit()
    conn.close()