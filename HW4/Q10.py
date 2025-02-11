import pandas as pd

poke_df = pd.read_csv("pokemon.csv")
encounters_df = pd.read_csv("encounters.csv")
location_area_df = pd.read_csv("location_areas.csv")
locations_df = pd.read_csv("locations.csv")

encounter_location_df = pd.merge(encounters_df, location_area_df, left_on='location_area_id', right_on='id', how='inner')

location_pokemon_df = pd.merge(encounter_location_df, locations_df, left_on='location_id', right_on='id', how='inner')

pokemon_location_count = location_pokemon_df.groupby('pokemon_id')['location_id'].nunique().reset_index(name='location_count')

most_locations_pokemon = pokemon_location_count.loc[pokemon_location_count['location_count'].idxmax()]
fewest_locations_pokemon = pokemon_location_count.loc[pokemon_location_count['location_count'].idxmin()]

most_locations_name = poke_df[poke_df['id'] == most_locations_pokemon['pokemon_id']]['identifier'].values[0]
fewest_locations_name = poke_df[poke_df['id'] == fewest_locations_pokemon['pokemon_id']]['identifier'].values[0]

result_df = pd.DataFrame({
    'pokemon_name': [most_locations_name, fewest_locations_name],
    'location_count': [most_locations_pokemon['location_count'], fewest_locations_pokemon['location_count']]
})

result_df.to_csv("q10.out", index=False)

print(result_df)
