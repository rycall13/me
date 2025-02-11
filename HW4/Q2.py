import pandas as pd

locations_df = pd.read_csv("locations.csv")

null_rows = locations_df[locations_df.isnull().any(axis=1)]

locations_df.loc[locations_df.isnull().any(axis=1), 'region'] = 999

locations_df.to_csv("q2-a.out", index=False)

print("Updated locations dataset written to q2-a.out")

regions_df = pd.read_csv("regions.csv")

new_region = pd.DataFrame({"region": [999], "identifier": ["Carlow"]})
regions_df = pd.concat([regions_df, new_region], ignore_index=True)

regions_df.to_csv("q2-b.out", index=False)

print("Updated regions dataset written to q2-b.out")
