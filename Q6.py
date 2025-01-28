import csv

pokemon_name = input("Enter the name of a Pokémon: ").strip().lower()

found = False
try:
    with open("poke.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            pokemon_id, name = row[0], row[1].lower()
            if name == pokemon_name:
                with open("q6.out", "w") as output_file:
                    output_file.write(f"ID: {pokemon_id}, Name: {row[1]}\n")
                print(f"Pokémon found: ID: {pokemon_id}, Name: {row[1]}")
                found = True
                break
        if not found:
            print("The Pokémon doesn't exist in the file.")

except Exception as e:
    print(f"An error occurred: {e}")