import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon_species.csv")


primary_types = df["primary_type"].value_counts().reset_index()
primary_types.columns = ["type", "count"]
primary_types["color"] = primary_types['type'].apply(lambda x: 'red' if x == 'fire' else 'blue') 


plt.figure(figsize=(12, 6))
plt.bar(primary_types["type"], primary_types["count"], color=primary_types["type_color"])
plt.xlabel("Pokémon Type")
plt.ylabel("Count")
plt.title("Number of Each Pokémon Type")
plt.xticks(rotation=45)
plt.show()
