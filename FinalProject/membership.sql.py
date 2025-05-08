import sqlite3

def create_membership_table():
    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS membership (
        team_id TEXT,
        pokemon_id INTEGER,
        PRIMARY KEY (team_id, pokemon_id),
        FOREIGN KEY (team_id) REFERENCES team(id),
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_membership_table()