import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon_types (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    );
''')

cursor.execute('''
    INSERT INTO pokemon_types (id, name)
    VALUES (999, 'unknown')
    ON CONFLICT(id) DO NOTHING;
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        height INTEGER,
        weight INTEGER,
        base_experience INTEGER,
        type_id INTEGER DEFAULT 999,
        FOREIGN KEY (type_id) REFERENCES pokemon_types(id)
    );
''')

conn.commit()
conn.close()