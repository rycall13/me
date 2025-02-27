import pandas as pd
import matplotlib.pyplot as plt

regions_df = pd.read_csv('regions.csv')
species_df = pd.read_csv('pokemon_species.csv')
generations_df = pd.read_csv('generations.csv')

region_counts = species_df['generation_id'].value_counts().reset_index()
region_counts.columns = ['generation_id', 'pokemon_count']

region_data = pd.merge(region_counts, generations_df[['id', 'main_region_id']], on='generation_id')
region_data = pd.merge(region_data, regions_df[['id', 'identifier']], left_on='main_region_id', right_on='id')

plt.figure(figsize=(10, 6))
plt.bar(region_data['identifier'], region_data['pokemon_count'], color='skyblue')

plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Pokémon', fontsize=12)
plt.title('Number of Pokémon in Each Region', fontsize=14)
plt.xticks(rotation=45)

plt.show()
