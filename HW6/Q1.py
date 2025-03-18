import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv("pokemon.csv")
types_df = pd.read_csv("types.csv")

type_counts = types_df["identifier"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(type_counts.index, type_counts.values, color="skyblue")

plt.xlabel("Pokémon Type")
plt.ylabel("Number of Pokémon")
plt.title("Number of Pokémon by Type")
plt.xticks(rotation=45)
plt.show()
