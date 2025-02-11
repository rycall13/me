import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

poke_df_cleaned = poke_df[poke_df['identifier'].str.contains('-', na=False)]

poke_df_cleaned['cleaned_name'] = poke_df_cleaned['identifier'].str.replace('-', '', regex=False)

unique_pokemon = poke_df_cleaned['cleaned_name'].drop_duplicates().reset_index(drop=True)

result_df = pd.DataFrame(unique_pokemon, columns=['cleaned_name'])

result_df.to_csv("q11.out", index=False)

print(result_df)
