import sqlite3

def create_trainer_table():
    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trainer (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        team_id TEXT,
        FOREIGN KEY (team_id) REFERENCES team(id)
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_trainer_table()