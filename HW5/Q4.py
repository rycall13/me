import pandas as pd
import matplotlib.pyplot as plt

pokemon_species = pd.read_csv('pokemon_species.csv')
pokemon_colors = pd.read_csv('pokemon_colors.csv')
pokemon_data = pd.read_csv('pokemon.csv')

q4_df = pd.merge(pokemon_species[['identifier', 'base_experience', 'color_id']], pokemon_colors[['id', 'identifier']], left_on='color_id', right_on='id')

q4_df.to_csv('Q4/q4.out', index=False)

sample_df = q4_df.sample(n=10)

plt.figure(figsize=(12, 6))
plt.bar(sample_df['identifier'], sample_df['base_experience'], color='green')

plt.xlabel('Pokémon', fontsize=12)
plt.ylabel('Base Experience', fontsize=12)
plt.title('Base Experience of Randomly Selected Pokémon', fontsize=14)
plt.xticks(rotation=45)

plt.show()