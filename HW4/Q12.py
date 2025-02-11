import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

def clean_name(name):
    cleaned_name = name.replace('-', ' ').title()
    return cleaned_name

poke_df['identifier'] = poke_df['identifier'].apply(clean_name)

poke_df.to_csv("q12.out", index=False)

print(poke_df[['identifier']])

