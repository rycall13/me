import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

cursor.execute('''
    DELETE FROM pokemon
    WHERE id > 10 OR weight < 30;
''')

conn.commit()

print("Deletion completed successfully.")

conn.close()
