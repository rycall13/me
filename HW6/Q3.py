import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")
rdf = pd.read_csv("types.csv")

df["identifier"] = df["identifier"].str.lower()

available_types = df["identifier"].unique()

while True:
    user_type = input("Enter a Pokémon: ").strip().lower()
    if user_type in available_types:
        break
    else:
        print("Invalid Pokemon! Please enter a valid Pokémon.")

filtered_df = df[df["identifier"] == user_type]

filtered_df["strength"] = (5 * filtered_df["height"]) + (2 * filtered_df["weight"]) + filtered_df["base_experience"]

generation_avg_strength = filtered_df.groupby("identifier")["strength"].mean()

plt.figure(figsize=(10, 5))
plt.plot(generation_avg_strength.index, generation_avg_strength.values, marker='o', linestyle='-', color="skyblue")

plt.xlabel("Generation")
plt.ylabel(f"Average Strength of {user_type.capitalize()} Pokémon")
plt.title(f"Average Strength of {user_type.capitalize()} Pokémon Over Generations")
plt.xticks(generation_avg_strength.index)
plt.show()
