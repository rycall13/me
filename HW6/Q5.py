import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pokemon.csv")

df["identifier"] = df["identifier"].str.lower()

def get_pokemon_stats(identifier):
    pokemon = df[df["identifier"] == identifier]
    if pokemon.empty:
        return None
    return {
        "identifier": pokemon.iloc[0]["identifier"].capitalize(),
        "height": pokemon.iloc[0]["height"],
        "weight": pokemon.iloc[0]["weight"],
        "base_experience": pokemon.iloc[0]["base_experience"]
    }

while True:
    poke1_name = input("Enter the first Pokémon name: ").strip().lower()
    poke1 = get_pokemon_stats(poke1_name)
    if poke1:
        break
    print("Invalid Pokémon name. Try again.")

while True:
    poke2_name = input("Enter the second Pokémon name: ").strip().lower()
    poke2 = get_pokemon_stats(poke2_name)
    if poke2:
        break
    print("Invalid Pokémon name. Try again.")

def calculate_strength(pokemon):
    return (5 * pokemon["height"]) + (2 * pokemon["weight"]) + pokemon["base_experience"]

poke1_strength = calculate_strength(poke1)
poke2_strength = calculate_strength(poke2)

def calculate_experience_progression(base_exp):
    levels = np.arange(0, 101)
    exp_values = base_exp * (levels / 100)
    return levels, exp_values

levels, poke1_exp = calculate_experience_progression(poke1["base_experience"])
_, poke2_exp = calculate_experience_progression(poke2["base_experience"])

poke1_total = poke1_strength + np.mean(poke1_exp)
poke2_total = poke2_strength + np.mean(poke2_exp)
winner = poke1["identifier"] if poke1_total > poke2_total else poke2["identifier"]

fig, axs = plt.subplots(3, 3, figsize=(12, 12))

axs[0, 1].axis("off")
axs[2, 1].axis("off")

axs[0, 0].bar(["Height", "Weight", "Base Exp"], [poke1["height"], poke1["weight"], poke1["base_experience"]], color="blue")
axs[0, 0].set_title(f"{poke1['identifier']} Stats")

axs[0, 2].bar(["Height", "Weight", "Base Exp"], [poke2["height"], poke2["weight"], poke2["base_experience"]], color="red")
axs[0, 2].set_title(f"{poke2['identifier']} Stats")

axs[2, 0].plot(levels, poke1_exp, color="blue")
axs[2, 0].set_title(f"{poke1['identifier']} Experience Over Levels")
axs[2, 0].set_xlabel("Level")
axs[2, 0].set_ylabel("Experience")

axs[2, 2].plot(levels, poke2_exp, color="red")
axs[2, 2].set_title(f"{poke2['identifier']} Experience Over Levels")
axs[2, 2].set_xlabel("Level")
axs[2, 2].set_ylabel("Experience")

axs[1, 1].text(0.5, 0.5, f"Winner: {winner}", fontsize=18, ha="center", va="center", fontweight="bold")
axs[1, 1].axis("off")

plt.tight_layout()
plt.show()
