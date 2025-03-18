import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

df["identifier"] = df["identifier"].str.lower()

available_types = df["identifier"].unique()

while True:
    user_type = input("Enter a Pokémon type: ").strip().lower()
    if user_type in available_types:
        break
    else:
        print("Invalid type! Please enter a valid Pokémon type.")

filtered_df = df[df["identifier"] == user_type]

filtered_df["strength"] = (5 * filtered_df["height"]) + (2 * filtered_df["weight"]) + filtered_df["base_experience"]

strength_stats = filtered_df.groupby("identifier")["strength"].agg(["mean", "min", "max"])

plt.figure(figsize=(10, 5))
plt.plot(strength_stats.index, strength_stats["mean"], marker='o', linestyle='-', color="blue", label="Average Strength")
plt.plot(strength_stats.index, strength_stats["min"], marker='o', linestyle='--', color="red", label="Minimum Strength")
plt.plot(strength_stats.index, strength_stats["max"], marker='o', linestyle='--', color="green", label="Maximum Strength")

plt.xlabel("Generation")
plt.ylabel(f"Strength of {user_type.capitalize()} Pokémon")
plt.title(f"Strength Statistics of {user_type.capitalize()} Pokémon Over Generations")
plt.xticks(strength_stats.index)
plt.legend() 
plt.show()
