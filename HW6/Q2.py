import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("types.csv")

df["identifier"] = df["identifier"].str.lower()

available_types = df["identifier"].unique()

while True:
    user_type = input("Enter a Pokémon type: ").strip().lower()
    if user_type in available_types:
        break
    else:
        print("Invalid type! Please enter a valid Pokémon type.")

filtered_df = df[df["identifier"] == user_type]

generation_counts = filtered_df["generation_id"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(generation_counts.index, generation_counts.values, color="skyblue")

plt.xlabel("Generation")
plt.ylabel(f"Number of {user_type.capitalize()} Pokémon")
plt.title(f"Number of {user_type.capitalize()} Pokémon in Each Generation")
plt.xticks(generation_counts.index)
plt.show()
