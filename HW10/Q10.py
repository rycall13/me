import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    height INTEGER CHECK(height > 1),
    weight INTEGER CHECK(weight < 1000),
    base_experience INTEGER
);
''')

conn.commit()

def insert_pokemon():
    try:
        id = int(input("Enter Pokémon ID (integer): "))
        name = input("Enter Pokémon name: ")
        height = int(input("Enter Pokémon height (must be >1): "))
        weight = int(input("Enter Pokémon weight (must be <1000): "))
        base_experience = int(input("Enter Pokémon base experience (integer): "))
        
        cursor.execute('''
            INSERT INTO pokemon (id, name, height, weight, base_experience)
            VALUES (?, ?, ?, ?, ?)
        ''', (id, name, height, weight, base_experience))
        
        conn.commit()
        print("✅ Pokémon inserted successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Insert failed: {e}")
    except sqlite3.OperationalError as e:
        print(f"Insert failed: {e}")
    except ValueError:
        print("Insert failed: Please make sure you are entering valid integer values where needed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

insert_pokemon()

conn.close()
