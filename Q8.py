import csv

pokemon_team = []
pokemon_locations = {}


def pokemon_exists(name):
    with open("poke.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if name.lower() == row[1].strip().lower():
                return row
    return None


def find_locations(pokemon_id):
    locations = []
    with open("locations.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == pokemon_id:
                locations.append(row[1].strip())
    return locations


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
            locations = find_locations(pokemon[0])
            pokemon_locations[pokemon[1]] = locations
            print(f"{pokemon[1]} has been added to your team!")
    else:
        print(f"The Pokémon '{user_input}' doesn't exist in the dataset.")


with open("q8.out", "w") as file:
    for pokemon in pokemon_team:
        name = pokemon[1]
        file.write(f"ID: {pokemon[0]}, Name: {name}\n")
        locations = pokemon_locations.get(name, [])
        if locations:
            file.write(f"  Locations: {', '.join(locations)}\n")
        else:
            file.write("  Locations: None found\n")


print("\nYour Pokémon team and their locations have been saved to 'q8.out'.")
print("Team members and their locations:")
for pokemon in pokemon_team:
    name = pokemon[1]
    print(f"ID: {pokemon[0]}, Name: {name}")
    locations = pokemon_locations.get(name, [])
    if locations:
        print(f"  Locations: {', '.join(locations)}")
    else:
        print("  Locations: None found")
