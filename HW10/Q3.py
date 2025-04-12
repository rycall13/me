import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT *
    FROM pokemon
    WHERE id BETWEEN 10 AND 35;
''')

results = cursor.fetchall()

with open('Q3.txt', 'w') as f:
    for row in results:
        f.write(str(row) + '\n')

conn.close()


