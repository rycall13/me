import sqlite3

def create_pokemon_table():
    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        height REAL,
        weight REAL,
        experience INTEGER
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_pokemon_table()