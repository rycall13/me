import sqlite3

def create_team_table():
    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        manager TEXT NOT NULL,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0,
        FOREIGN KEY (manager) REFERENCES trainer(id)
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_team_table()