import pandas as pd

poke_df = pd.read_csv("pokemon.csv")
poke_types_df = pd.read_csv("pokemon_types.csv")
types_df = pd.read_csv("types.csv")

fire_type_id = types_df[types_df['identifier'].str.lower() == 'fire']['id'].values

fire_pokemon_ids = poke_types_df[poke_types_df['type_id'].isin(fire_type_id)]['pokemon_id'].values

remaining_pokemon_df = poke_df[~poke_df['id'].isin(fire_pokemon_ids)]

remaining_count = len(remaining_pokemon_df)

with open("q8.out", "w") as file:
    file.write(str(remaining_count))

print(f"Number of remaining Pokémon written to q8.out: {remaining_count}")
