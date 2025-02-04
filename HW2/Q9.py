import pandas as pd

pokemon_df = pd.read_csv('poke.csv')

team = []

def add_to_team(pokemon_name):
    if len(team) >= 6:
        print("Too many team members")
        return
    
    if pokemon_name not in pokemon_df['identifier'].values:
        print("This pokemon does not exist")
        return

    team.append(pokemon_name)
    print(f"{pokemon_name} added to the team.")

def drop_from_team(pokemon_name):
    if pokemon_name not in team:
        print(f"{pokemon_name} is not in your team.")
        return

    team.remove(pokemon_name)
    print(f"{pokemon_name} has been removed from your team.")

def print_team():
    if not team:
        print("Your team is empty.")
        return

    print("Your current team members:")
    team_df = pokemon_df[pokemon_df['identifier'].isin(team)]
    print(team_df)

def main_menu():
    while True:
        print("\n--- Team Builder Menu ---")
        print("a. Add To Team")
        print("b. Drop From Team")
        print("c. Print Team")
        print("d. Exit")
        
        choice = input("Please choose an option: ").lower()
        
        if choice == 'a':
            pokemon_name = input("Enter the Pokémon name to add: ")
            add_to_team(pokemon_name)
        elif choice == 'b':
            pokemon_name = input("Enter the Pokémon name to drop: ")
            drop_from_team(pokemon_name)
        elif choice == 'c':
            print_team()
        elif choice == 'd':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
