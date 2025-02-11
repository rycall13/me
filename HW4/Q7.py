import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

def modify_name(row):
    if row['height'] > 100:
        return row['identifier'].upper()
    elif 50 <= row['height'] <= 60:
        return row['identifier'].title()
    elif row['height'] < 50:
        return row['identifier'].lower()
    return row['identifier']

poke_df['identifier'] = poke_df.apply(modify_name, axis=1)

poke_df.to_csv("q7.out", index=False)

print("Modified Pokémon dataset written to q7.out")
