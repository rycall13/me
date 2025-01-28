import csv

pokemon_team = []


def pokemon_exists(name):
        with open("poke.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if name.lower() == row[1].strip().lower():
                    return row
        return None


while len(pokemon_team) < 6:
    user_input = input("Enter the name of a Pokémon to add to your team (or type 'exit' to finish): ").strip()
    
    if user_input.lower() == "exit":
        break

    pokemon = pokemon_exists(user_input)
    if pokemon:
        if pokemon in pokemon_team:
            print(f"{pokemon[1]} is already in your team!")
        else:
            pokemon_team.append(pokemon)
            print(f"{pokemon[1]} has been added to your team!")
    else:
        print(f"The Pokémon '{user_input}' doesn't exist in the dataset.")


with open("q7.out", "w") as file:
    for pokemon in pokemon_team:
        file.write(f"ID: {pokemon[0]}, Name: {pokemon[1]}\n")


print("\nYour Pokémon team has been saved to 'q7.out'.")
print("Team members:")
for pokemon in pokemon_team:
    print(f"ID: {pokemon[0]}, Name: {pokemon[1]}")
