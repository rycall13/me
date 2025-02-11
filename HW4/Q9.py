import pandas as pd

poke_df = pd.read_csv("pokemon.csv")
encounters_df = pd.read_csv("encounters.csv")
location_area_df = pd.read_csv("location_areas.csv")
locations_df = pd.read_csv("locations.csv")


encounter_location_df = pd.merge(encounters_df, location_area_df, left_on='location_area_id', right_on='id', how='inner')

location_pokemon_df = pd.merge(encounter_location_df, locations_df, left_on='location_id', right_on='id', how='inner')

location_counts = location_pokemon_df.groupby('identifier_x').size().reset_index(name='pokemon_count')

top_locations = location_counts.sort_values(by='pokemon_count', ascending=False).head(5)

print(top_locations)

top_locations.to_csv("top_5_locations.csv", index=False)
