import random
import pandas as pd
from flask import Flask

poke_df = pd.read_csv('pokemon.csv')

app = Flask(__name__)

@app.route('/')
def random_pokemon():
    return random.choice(poke_df["identifier"].tolist())

def hello_pokemon():
    return f"Hello, {random_pokemon()}!"

app.run(host='127.0.0.1', port=9999, debug=False)