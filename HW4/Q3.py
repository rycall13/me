import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

vowels = ('a', 'e', 'i', 'o', 'u')

vowel_pokemon = poke_df[poke_df['identifier'].str.startswith(vowels, na=False)]

vowel_pokemon.to_csv("q3.out", index=False)

print("Filtered Pokémon dataset written to q3.out")
