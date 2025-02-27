import pandas as pd

pokemon_species = pd.read_csv('pokemon_species.csv')
generations = pd.read_csv('generations.csv')

merged_df = pokemon_species[['identifier', 'generation_id']].merge(generations[['id']], left_on='generation_id', right_on='id', how='left')

merged_df.to_csv('q1.out', index=False)

merged_df[['identifier', 'generation_id']].to_csv('q1.csv', index=False)
