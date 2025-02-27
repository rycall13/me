import pandas as pd

df = pd.read_csv("pokemon_species.csv")

legendaries = df[(df['is_mythical'] == 1) | (df['is_legendary'] == 1)]

legendaries.to_cvs('Q7/q7.out', index=False)