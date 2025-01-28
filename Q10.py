import random


dungeon_width = 4
dungeon_height = 2


dungeon = [[(x, y) for x in range(dungeon_width)] for y in range(dungeon_height)]


start_position = (random.randint(0, dungeon_width - 1), random.randint(0, dungeon_height - 1))
exit_position = (random.randint(0, dungeon_width - 1), random.randint(0, dungeon_height - 1))


while exit_position == start_position:
    exit_position = (random.randint(0, dungeon_width - 1), random.randint(0, dungeon_height - 1))


current_position = start_position
move_count = 0
success = False

print("Welcome to the dungeon!")
print(f"The dungeon is {dungeon_width} squares wide and {dungeon_height} squares deep.")
print(f"Your starting position is {current_position}. Find the exit!")


def get_movement_options(position):
    x, y = position
    options = []
    if x > 0: options.append("left")
    if x < dungeon_width - 1: options.append("right")
    if y > 0: options.append("up")
    if y < dungeon_height - 1: options.append("down")
    return options

# Game loop
while True:
    print(f"\nYou are currently at {current_position}.")
    if current_position == exit_position:
        success = True
        print("Congratulations! You've found the exit!")
        break

    movement_options = get_movement_options(current_position)
    print(f"Your movement options are: {', '.join(movement_options)}")
    print("Or type 'exit' to leave the game.")
    user_input = input("What would you like to do? ").strip().lower()

    if user_input == "exit":
        print("You chose to leave the game.")
        break

    if user_input in movement_options:
        x, y = current_position
        if user_input == "left":
            current_position = (x - 1, y)
        elif user_input == "right":
            current_position = (x + 1, y)
        elif user_input == "up":
            current_position = (x, y - 1)
        elif user_input == "down":
            current_position = (x, y + 1)
        move_count += 1
        print(f"You moved {user_input} to {current_position}.")
    else:
        print("Invalid move. Try again.")

# Write results to file
with open("q10.out", "w") as file:
    file.write(f"success={success}\n")
    file.write(f"moves={move_count}\n")

# Final output
if success:
    print(f"You reached the exit in {move_count} moves. Your results have been saved to 'q10.out'.")
else:
    print(f"You left the game after {move_count} moves. Your results have been saved to 'q10.out'.")
