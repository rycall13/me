import sqlite3
import csv

conn = sqlite3.connect('poke.db')
cur = conn.cursor()

cur.execute('DELETE FROM pokemon WHERE id > 50')

type_mapping = {}
with open('pokemon_types.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        type_mapping[row['id']] = row['type_id']

for poke in cur.execute('SELECT id FROM pokemon').fetchall():
    poke_id = str(poke[0])
    if poke_id in type_mapping:
        type_id = type_mapping[poke_id]
        cur.execute('''
        UPDATE pokemon
        SET type_id = ?
        WHERE id = ?
        ''', (type_id, poke_id))

conn.commit()
conn.close()
