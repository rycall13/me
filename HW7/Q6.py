from flask import Flask, jsonify
import pandas as pd
import random

poke_df = pd.read_csv('pokemon.csv')

app = Flask(__name__)

team = []

out_log = "../Q6/out.log"
def log(action, method, pokemon=None):
    with open(out_log, "a") as f:
        entry = f"{action} - {method}"
        if pokemon:
            entry += f" - {pokemon}"
        f.write(entry + "/n")
        
        
@app.route('/create', methods=['POST'])
def create_team():
    global team
    if team:
        return "A team already exists!"
    team = random.sample(poke_df["identifier"].tolist(), 6)
    log("Team Created", "POST", ", ".join(team))
    return jsonify(team) 

@app.route('/list', methods=['GET'])
def list_team():
    if not team:
        return "No team exists!"
    log("Team Listed", "GET")
    return jsonify(team)

@app.route('/delete', methods=['DELETE'])
def delete_team():
    global team
    if not team:
        return "No team to delete!"
    log("Team Deleted", "DELETE", ", ".join(team))
    team = []
    return "Team deleted!"

app.run(host='127.0.0.1', port=8989, debug=False)