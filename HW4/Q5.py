import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

while True:
    user_input = input("Enter a single letter to find Pokémon: ").strip().lower()
    
    if len(user_input) == 1 and user_input.isalpha():
        break
    else:
        print("Invalid input! Please enter only one letter.")

filtered_pokemon = poke_df[poke_df['identifier'].str.lower().str.startswith(user_input, na=False)]

if filtered_pokemon.empty:
    print("No Pokémon found starting with that letter.")
else:
    max_strength = filtered_pokemon['base_experience'].max()

    strongest_pokemon = filtered_pokemon[filtered_pokemon['base_experience'] == max_strength]

    strongest_pokemon = strongest_pokemon.sort_values(by='identifier', ascending=True)

    strongest_pokemon.to_csv("q5.out", index=False)

    print("Strongest Pokémon written to q5.out")
