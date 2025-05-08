from flask import Flask, jsonify, request
import sqlite3
import logging

app = Flask(__name__)

logging.basicConfig(filename='teambattle.log', level=logging.DEBUG)

def get_db_connection():
    conn = sqlite3.connect('teambattle.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_id = request.args.get('id')
    name = request.args.get('name')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if pokemon_id:
        cursor.execute('SELECT * FROM pokemon WHERE id = ?', (pokemon_id,))
    elif name:
        cursor.execute('SELECT * FROM pokemon WHERE name LIKE ?', ('%' + name + '%',))
    
    pokemon = cursor.fetchone()
    conn.close()

    if pokemon:
        return jsonify({
            "Error": "",
            "Message": "Pokemon found",
            "Object": {"Pokemon": dict(pokemon)}
        }), 200
    else:
        return jsonify({
            "Error": "Pokemon not found",
            "Message": "No pokemon matching the criteria",
            "Object": {}
        }), 400

@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    data = request.get_json()
    name = data['name']
    height = data['height']
    weight = data['weight']
    experience = data['experience']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pokemon (name, height, weight, experience)
        VALUES (?, ?, ?, ?)
    ''', (name, height, weight, experience))
    conn.commit()
    conn.close()

    logging.debug(f"Pokemon created: {name}")
    return jsonify({
        "Error": "",
        "Message": "Pokemon created successfully",
        "Object": {}
    }), 201

@app.route('/trainer', methods=['GET'])
def get_trainer():
    trainer_id = request.args.get('id')
    name = request.args.get('name')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if trainer_id:
        cursor.execute('SELECT * FROM trainer WHERE id = ?', (trainer_id,))
    elif name:
        cursor.execute('SELECT * FROM trainer WHERE name LIKE ?', ('%' + name + '%',))
    
    trainer = cursor.fetchone()
    conn.close()

    if trainer:
        return jsonify({
            "Error": "",
            "Message": "Trainer found",
            "Object": {"Trainer": dict(trainer)}
        }), 200
    else:
        return jsonify({
            "Error": "Trainer not found",
            "Message": "No trainer matching the criteria",
            "Object": {}
        }), 400

@app.route('/trainer', methods=['POST'])
def create_trainer():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trainer (name, email, phone)
        VALUES (?, ?, ?)
    ''', (name, email, phone))
    conn.commit()
    conn.close()

    logging.debug(f"Trainer created: {name}")
    return jsonify({
        "Error": "",
        "Message": "Trainer created successfully",
        "Object": {}
    }), 201

@app.route('/trainer/<int:id>', methods=['DELETE'])
def delete_trainer(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM trainer WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    logging.debug(f"Trainer deleted: {id}")
    return jsonify({
        "Error": "",
        "Message": "Trainer deleted successfully",
        "Object": {}
    }), 200

@app.route('/team', methods=['GET'])
def get_team():
    team_id = request.args.get('id')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if team_id:
        cursor.execute('SELECT * FROM team WHERE id = ?', (team_id,))
    
    team = cursor.fetchone()
    conn.close()

    if team:
        return jsonify({
            "Error": "",
            "Message": "Team found",
            "Object": {"Team": dict(team)}
        }), 200
    else:
        return jsonify({
            "Error": "Team not found",
            "Message": "No team matching the criteria",
            "Object": {}
        }), 400

@app.route('/team', methods=['POST'])
def create_team():
    data = request.get_json()
    name = data['name']
    manager_id = data['manager_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO team (name, manager_id)
        VALUES (?, ?)
    ''', (name, manager_id))
    conn.commit()
    conn.close()

    logging.debug(f"Team created: {name}")
    return jsonify({
        "Error": "",
        "Message": "Team created successfully",
        "Object": {}
    }), 201

@app.route('/team/<int:id>', methods=['DELETE'])
def delete_team(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM team WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    logging.debug(f"Team deleted: {id}")
    return jsonify({
        "Error": "",
        "Message": "Team deleted successfully",
        "Object": {}
    }), 200

@app.route('/membership', methods=['POST'])
def add_membership():
    data = request.get_json()
    team_id = data['team_id']
    pokemon_id = data['pokemon_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO membership (team_id, pokemon_id)
        VALUES (?, ?)
    ''', (team_id, pokemon_id))
    conn.commit()
    conn.close()

    logging.debug(f"Pokemon {pokemon_id} added to team {team_id}")
    return jsonify({
        "Error": "",
        "Message": "Pokemon added to team successfully",
        "Object": {}
    }), 201

@app.route('/membership', methods=['DELETE'])
def remove_membership():
    data = request.get_json()
    team_id = data['team_id']
    pokemon_id = data['pokemon_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM membership WHERE team_id = ? AND pokemon_id = ?
    ''', (team_id, pokemon_id))
    conn.commit()
    conn.close()

    logging.debug(f"Pokemon {pokemon_id} removed from team {team_id}")
    return jsonify({
        "Error": "",
        "Message": "Pokemon removed from team successfully",
        "Object": {}
    }), 200

@app.route('/ranking', methods=['GET'])
def get_ranking():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, name, wins, losses FROM team
        ORDER BY (wins - losses) DESC LIMIT 3
    ''')
    teams = cursor.fetchall()
    conn.close()

    ranking = [{"id": team["id"], "name": team["name"], "wins": team["wins"], "losses": team["losses"]} for team in teams]

    return jsonify({
        "Error": "",
        "Message": "Top teams",
        "Object": {"Ranking": ranking}
    }), 200

@app.route('/battle', methods=['POST'])
def battle():
    data = request.get_json()
    team1_id = data['team1_id']
    team2_id = data['team2_id']
    
    if team1_id == team2_id:
        return jsonify({
            "Error": "Teams cannot battle themselves",
            "Message": "A team cannot battle itself",
            "Object": {}
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT SUM(experience) FROM pokemon WHERE id IN (SELECT pokemon_id FROM membership WHERE team_id = ?)', (team1_id,))
    team1_exp = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(experience) FROM pokemon WHERE id IN (SELECT pokemon_id FROM membership WHERE team_id = ?)', (team2_id,))
    team2_exp = cursor.fetchone()[0]
    
    if team1_exp > team2_exp:
        winner = team1_id
        loser = team2_id
    elif team2_exp > team1_exp:
        winner = team2_id
        loser = team1_id
    else:
        return jsonify({
            "Error": "",
            "Message": "It's a draw",
            "Object": {}
        }), 200

    cursor.execute('UPDATE team SET wins = wins + 1 WHERE id = ?', (winner,))
    cursor.execute('UPDATE team SET losses = losses + 1 WHERE id = ?', (loser,))
    conn.commit()
    conn.close()

    return jsonify({
        "Error": "",
        "Message": f"Battle result: Team {winner} wins",
        "Object": {}
    }), 200

if __name__ == '__main__':
    app.run(debug=False)
