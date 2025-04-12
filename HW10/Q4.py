import sqlite3
import csv

conn = sqlite3.connect('poke.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

with open('pokemon_type_names.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['local_language_id'] == '9':
            cur.execute('''
            INSERT OR IGNORE INTO pokemon_types (id, name)
            VALUES (?, ?)
            ''', (row['type_id'], row['name']))

conn.commit()
conn.close()
