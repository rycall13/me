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

def list_team():
    if not pokemon_team:
        print("Your team is currently empty.")
        return
    print("Current Team:")
    for idx, pokemon in enumerate(pokemon_team, 1):
        print(f"{idx}) {pokemon[1]}")


def drop_member():
    if not pokemon_team:
        print("Your team is currently empty. Nothing to remove.")
        return
    list_team()
    try:
        member_id = int(input("Enter the ID of the member you want to remove: "))
        if 1 <= member_id <= len(pokemon_team):
            removed = pokemon_team.pop(member_id - 1)
            del pokemon_locations[removed[1]]
            print(f"{removed[1]} has been removed from your team.")
        else:
            print("Invalid ID. Please choose a valid team member.")
    except ValueError:
        print("Invalid input. Please enter a number.")


while True:
    print("\nMenu:")
    print("1) Add Pokémon")
    print("2) List Team")
    print("3) Drop Member")
    print("4) Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        if len(pokemon_team) >= 6:
            print("Your team is full. Remove a member to add a new one.")
            continue
        user_input = input("Enter the name of a Pokémon to add to your team: ").strip()
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

    elif choice == "2":
        list_team()

    elif choice == "3":
        drop_member()

    elif choice == "4":

        with open("q9.out", "w") as file:
            for pokemon in pokemon_team:
                name = pokemon[1]
                file.write(f"ID: {pokemon[0]}, Name: {name}\n")
                locations = pokemon_locations.get(name, [])
                if locations:
                    file.write(f"  Locations: {', '.join(locations)}\n")
                else:
                    file.write("  Locations: None found\n")
        print("Your Pokémon team has been saved to 'q9.out'. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
