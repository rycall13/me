import sqlite3
import csv

conn = sqlite3.connect('poke.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER
)
''')

with open('pokemon.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        c.execute('''
        INSERT OR IGNORE INTO pokemon (id, name, height, weight, base_experience)
        VALUES (?, ?, ?, ?, ?)
        ''', (row['id'], row['identifier'], row['height'], row['weight'], row['base_experience']))

conn.commit()
conn.close()
