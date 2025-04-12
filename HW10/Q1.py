import sqlite3


conn = sqlite3.connect('poke.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        height INTEGER,
        weight INTEGER,
        base_experience INTEGER
        );
    ''')
