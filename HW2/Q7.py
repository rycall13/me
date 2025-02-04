import pandas as pd

def summarize_pokemon_data(file_path):
    try:
        df = pd.read_csv(file_path)
        
        while True:
            pokemon_name = input("Enter the name of a Pokemon (or type 'exit' to quit): ")
            if pokemon_name.lower() == 'exit':
                print("Exiting...")
                break
            
            filtered_df = df[df['identifier'].str.lower() == pokemon_name.lower()]
            
            if not filtered_df.empty:
                print(filtered_df)
            else:
                print("This pokemon does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")

summarize_pokemon_data('poke.csv')
