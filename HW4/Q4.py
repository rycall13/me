import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

p_pokemon = poke_df[poke_df['identifier'].str.startswith('p', na=False)]

max_strength = p_pokemon['base_experience'].max()

strongest_p_pokemon = p_pokemon[p_pokemon['base_experience'] == max_strength]

strongest_p_pokemon = strongest_p_pokemon.sort_values(by='identifier', ascending=False)

strongest_p_pokemon.to_csv("q4.out", index=False)

print("Strongest 'p' Pokémon written to q4.out")
