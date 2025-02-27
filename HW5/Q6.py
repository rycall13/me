import pandas as pd

df = pd.read_csv("pokemon_species.csv")

secondary_types = df['secondary_type'].value_counts()
most_common_type = secondary_types.idxmax()
most_common_count = secondary_types.max()

with open('Q6/q6.out', 'w') as f:
    f.write(f"{most_common_type},{most_common_count}/n")