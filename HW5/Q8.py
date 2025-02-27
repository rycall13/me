import pandas as pd
import matplotlib.pyplot as plt


legendaries = pd.read_csv("pokemon.csv")

legendaries['Strength'] =(legendaries['base_experience'] * 5) + ((legendaries['height'] + legendaries['weight']))
strongest = legendaries.sort_values('Strength', ascending=False).head(5)
strongest.to_csv('Q8/q8.out', index=False)

plt.figure(figsize=(12, 6))
plt.bar(strongest["identifier"], strongest["Strength"], color='blue')
plt.xlabel("Pokémon")
plt.ylabel("Strength")
plt.title("Strongest Pokemon")
plt.xticks(rotation=45)
plt.show()