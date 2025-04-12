import sqlite3
import csv

conn = sqlite3.connect('poke.db')
cur = conn.cursor()

with open('pokemon.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute('''
        INSERT INTO pokemon (id, name, height, weight, base_experience, type_id)
        VALUES (?, ?, ?, ?, ?, 999)
        ''', (row['id'], row['identifier'], row['height'], row['weight'], row['base_experience']))

conn.commit()
conn.close()