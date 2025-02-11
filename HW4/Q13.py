import pandas as pd

poke_df = pd.read_csv("pokemon.csv")

def save_to_file():
    poke_df.to_csv("q13.out", index=False)
    print("Changes saved to q13.out.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("a. Manage Dataset")
        print("b. Exit")
        choice = input("Choose an option (a/b): ").lower()

        if choice == 'a':
            manage_dataset()
        elif choice == 'b':
            save_to_file()
            break
        else:
            print("Invalid option. Please choose 'a' or 'b'.")

def manage_dataset():
    while True:
        print("\nManage Dataset Menu:")
        print("1. Add Pokemon")
        print("2. Delete Pokemon")
        print("3. Update Pokemon")
        print("4. Go Back to Main Menu")
        action = input("Choose an option (1/2/3/4): ")

        if action == '1':
            add_pokemon()
        elif action == '2':
            delete_pokemon()
        elif action == '3':
            update_pokemon()
        elif action == '4':
            break
        else:
            print("Invalid option. Please choose a valid action.")

def add_pokemon():
    print("\nAdding a new Pokémon.")
    name = input("Enter the Pokémon name: ")
    height = input("Enter the Pokémon height: ")
    weight = input("Enter the Pokémon weight: ")
    species_id = input("Enter the species ID: ")

    new_pokemon = {
        'id': poke_df['id'].max() + 1,
        'identifier': name,
        'height': height,
        'weight': weight,
        'species_id': species_id
    }

    poke_df.loc[len(poke_df)] = new_pokemon
    print(f"{name} has been added to the dataset.")

def delete_pokemon():
    try:
        pokemon_id = int(input("\nEnter the ID of the Pokémon to delete: "))
        if pokemon_id in poke_df['id'].values:
            poke_df.drop(poke_df[poke_df['id'] == pokemon_id].index, inplace=True)
            print(f"Pokémon with ID {pokemon_id} has been deleted.")
        else:
            print("Pokémon ID not found.")
    except ValueError:
        print("Please enter a valid integer ID.")

def update_pokemon():
    try:
        pokemon_id = int(input("\nEnter the ID of the Pokémon to update: "))
        if pokemon_id in poke_df['id'].values:
            new_name = input("Enter the new name for the Pokémon: ")
            poke_df.loc[poke_df['id'] == pokemon_id, 'identifier'] = new_name
            print(f"Pokémon with ID {pokemon_id} has been updated to {new_name}.")
        else:
            print("Pokémon ID not found.")
    except ValueError:
        print("Please enter a valid integer ID.")

main_menu()
