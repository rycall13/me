from flask import Flask
import pandas as pd
import random

poke_df = pd.read_csv('pokemon.csv')

app = Flask(__name__)

team = []


@app.route('/create', methods=['POST'])
def create_team():
    global team
    if team:
        return "A team already exists!"
    team = random.sample(poke_df["identifier"].tolist(), 6)
    return team 

@app.route('/list', methods=['GET'])
def list_team():
    if not team:
        return "No team exists!"
    return team

@app.route('/delete', methods=['DELETE'])
def delete_team():
    global team
    if not team:
        return "No team to delete!"
    team = []
    return "Team deleted!"

app.run(host='127.0.0.1', port=8989, debug=False)