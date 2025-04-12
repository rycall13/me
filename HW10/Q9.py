import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

query = '''
SELECT p.name AS pokemon_name, pt.name AS type_name
FROM pokemon p
JOIN pokemon_types pt ON p.type_id = pt.id;
'''

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Pokemon: {row[0]}, Type: {row[1]}")

with open('Q9.txt', 'w') as f:
    for row in results:
        f.write(f"Pokemon: {row[0]}, Type: {row[1]}\n")

conn.close()