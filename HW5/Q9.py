import pandas as pd
import random

df = pd.read_csv("pokemon.csv")

def get_random_pokemon():
    return df.sample(1).iloc[0]

dungeon = [[get_random_pokemon() for _ in range(4)] for _ in range(4)]

start_x, start_y = random.randint(0, 3), random.randint(0, 3)
exit_x, exit_y = random.randint(0, 3), random.randint(0, 3)
while (start_x, start_y) == (exit_x, exit_y):
    exit_x, exit_y = random.randint(0, 3), random.randint(0, 3)

def create_team():
    choice = input("Do you want to select your Pokémon team (y/n)? ").strip().lower()
    team = []
    if choice == 'y':
        print("Available Pokémon:")
        print(df[['identifier', 'base_experience']].head(20))
        for _ in range(6):
            name = input("Enter Pokémon name: ").strip().lower()
            selected_pokemon = df[df["identifier"] == name]
            if not selected_pokemon.empty:
                team.append(selected_pokemon.iloc[0])
            else:
                print("Invalid Pokémon name. Try again.")
    else:
        team = [get_random_pokemon() for _ in range(6)]
    return team

team = create_team()
player_x, player_y = start_x, start_y

while team:
    print(f"\nCurrent Position: ({player_x}, {player_y})")
    
    move = input("Move (up/down/left/right) or type 'exit' to quit: ").strip().lower()
    if move == "exit":
        with open("status.out", "w") as f:
            f.write("failure")
        print("You exited the dungeon. Game over!")
        break

    if move == "up" and player_x > 0:
        player_x -= 1
    elif move == "down" and player_x < 3:
        player_x += 1
    elif move == "left" and player_y > 0:
        player_y -= 1
    elif move == "right" and player_y < 3:
        player_y += 1
    else:
        print("Invalid move. Try again.")
        continue

    if (player_x, player_y) == (exit_x, exit_y):
        with open("status.out", "w") as f:
            f.write(f"success, remaining team members: {len(team)}")
        print("You found the exit! Congratulations!")
        break

    encountered_pokemon = dungeon[player_x][player_y]
    print(f"You encountered {encountered_pokemon['identifier']} (Base XP: {encountered_pokemon['base_experience']})")

    player_pokemon = team[0]
    if player_pokemon["base_experience"] > encountered_pokemon["base_experience"]:
        print(f"{player_pokemon['identifier']} defeated {encountered_pokemon['identifier']}!")
    else:
        print(f"{player_pokemon['identifier']} was defeated and removed from your team!")
        team.pop(0)

    if not team:
        with open("status.out", "w") as f:
            f.write("failure")
        print("Your team has been defeated. Game over!")
        break
