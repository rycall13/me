from flask import Flask, request, jsonify
import sqlite3
import random
import logging

app = Flask(__name__)

logging.basicConfig(filename='teambattle.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

def ensure_strength_column():
    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE membership ADD COLUMN strength INTEGER DEFAULT 0")
        app.logger.debug("Added 'strength' column to 'membership' table.")
    except sqlite3.OperationalError:
        app.logger.debug("'strength' column already exists.")
    conn.commit()
    conn.close()

ensure_strength_column()

@app.route('/')
def index():
    return jsonify({
        "Error": "",
        "Message": "Welcome to the Team Battle API with Pokémon Training!",
        "Object": {}
    })

@app.route('/train', methods=['POST'])
def train_pokemon():
    data = request.get_json()
    team_id = data.get('team_id')
    pokemon_id = data.get('pokemon_id')

    if not team_id or not pokemon_id:
        return jsonify({
            "Error": "Missing team_id or pokemon_id",
            "Message": "You must provide both team_id and pokemon_id to train.",
            "Object": {}
        }), 400

    conn = sqlite3.connect('teambattle.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM membership WHERE team_id = ? AND pokemon_id = ?", (team_id, pokemon_id))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return jsonify({
            "Error": "Membership not found",
            "Message": "The specified Pokémon is not part of that team.",
            "Object": {}
        }), 400

    increase = random.randint(0, 10)

    cursor.execute("UPDATE membership SET strength = strength + ? WHERE team_id = ? AND pokemon_id = ?",
                   (increase, team_id, pokemon_id))

    cursor.execute("SELECT strength FROM membership WHERE team_id = ? AND pokemon_id = ?", (team_id, pokemon_id))
    updated_strength = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    app.logger.debug(f"Trained Pokémon {pokemon_id} on Team {team_id} for +{increase} strength (new: {updated_strength})")

    return jsonify({
        "Error": "",
        "Message": f"Trained Pokémon {pokemon_id} for +{increase} strength!",
        "Object": {
            "team_id": team_id,
            "pokemon_id": pokemon_id,
            "new_strength": updated_strength
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=False)
