import pandas as pd

def summarize_pokemon_data(file_path):
    try:
        df = pd.read_csv(file_path)
        
        while True:
            user_input = input("Enter a number: ")
            
            if user_input.isdigit():
                number = int(user_input)

                index_data = df.iloc[[number]] if number < len(df) else pd.DataFrame()

                id_data = df[df['identifier'] == number]
                
                result = pd.concat([index_data, id_data]).drop_duplicates()
                
                if not result.empty:
                    print(result)
                else:
                    print("No matching Pokémon found.")
            else:
                print("Please provide a number")
                user_input = input("Enter a number: ")
                if not user_input.isdigit():
                    print("Error")
                    break
    except Exception as e:
        print(f"Error reading file: {e}")

summarize_pokemon_data('poke.csv')
