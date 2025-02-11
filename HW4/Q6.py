import pandas as pd

poke_df = pd.read_csv("pokemon.csv")
poke_types_df = pd.read_csv("pokemon_types.csv")
types_df = pd.read_csv("types.csv")

user_pokemon = input("Enter a Pokémon name: ").strip().lower()

if user_pokemon not in poke_df['identifier'].str.lower().values:
    result = "pokemon does not exist"
    print(result)
else:
    pokemon_data = poke_df[poke_df['identifier'].str.lower() == user_pokemon]
    pokemon_id = pokemon_data['id'].values[0]

    type_ids = poke_types_df[poke_types_df['pokemon_id'] == pokemon_id]['type_id'].values

    pokemon_types = types_df[types_df['id'].isin(type_ids)]['identifier'].values

    matching_pokemon_ids = poke_types_df[poke_types_df['type_id'].isin(type_ids)]['pokemon_id'].values
    matching_pokemon = poke_df[poke_df['id'].isin(matching_pokemon_ids)]

    type_count = len(matching_pokemon)

    strongest_pokemon = matching_pokemon.loc[matching_pokemon['base_experience'].idxmax()]['identifier']
    weakest_pokemon = matching_pokemon.loc[matching_pokemon['base_experience'].idxmin()]['identifier']

    result = (
        f"Type(s): {', '.join(pokemon_types)}\n"
        f"Total Pokémon of this type: {type_count}\n"
        f"Strongest Pokémon: {strongest_pokemon}\n"
        f"Weakest Pokémon: {weakest_pokemon}"
    )
    print(result)

with open("q6.out", "w") as file:
    file.write(result)
