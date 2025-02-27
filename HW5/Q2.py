import pandas as pd
import random
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('pokemon.csv')
pokemon_df['identifier'] = pokemon_df['identifier'].str.lower()

pokemon_team = []

def add_pokemon():
    if len(pokemon_team) >= 6:
        print("Your team is full (max 6 Pokémon)!")
        return

    name = input("Enter the Pokémon name: ").strip().lower()
    if name in pokemon_df['identifier'].values:
        if name not in pokemon_team:
            pokemon_team.append(name)
            print(f"{name.capitalize()} has been added to your team!")
        else:
            print(f"{name.capitalize()} is already in your team!")
    else:
        print("Invalid Pokémon name. Please try again.")

def generate_random_team():
    global pokemon_team
    pokemon_team = random.sample(list(pokemon_df['identifier']), min(6, len(pokemon_df)))
    print("Random team generated:", ", ".join(pokemon.capitalize() for pokemon in pokemon_team))

def delete_pokemon():
    if not pokemon_team:
        print("Your team is empty!")
        return

    name = input("Enter the Pokémon name to remove: ").strip().lower()
    if name in pokemon_team:
        pokemon_team.remove(name)
        print(f"{name.capitalize()} has been removed from your team!")
    else:
        print(f"{name.capitalize()} is not in your team.")

def show_team_experience():
    if not pokemon_team:
        print("No Pokémon in the team to display.")
        return

    team_data = pokemon_df[pokemon_df['identifier'].isin(pokemon_team)]
    plt.figure(figsize=(10, 5))
    plt.bar(team_data['identifier'].str.capitalize(), team_data['base_experience'], color='skyblue')
    plt.xlabel("Pokémon")
    plt.ylabel("Base Experience")
    plt.title("Base Experience of Pokémon in Team")
    plt.xticks(rotation=45)
    plt.show()

def main():
    while True:
        print("\nPokémon Team Builder")
        print("1. Add Pokémon")
        print("2. Generate Random Team")
        print("3. Delete Pokémon")
        print("4. Exit & Show Team Stats")
        
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_pokemon()
        elif choice == '2':
            generate_random_team()
        elif choice == '3':
            delete_pokemon()
        elif choice == '4':
            show_team_experience()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
