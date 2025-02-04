import pandas as pd

def main_menu(pokemon_file, regions_file, locations_file):
    try:
        pokemon_df = pd.read_csv(pokemon_file)
        regions_df = pd.read_csv(regions_file)
        locations_df = pd.read_csv(locations_file)
        
        while True:
            print("\nHello, Ash!")
            print("1) Search By Name")
            print("2) Search By Region")
            print("3) Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                pokemon_name = input("Enter a Pokemon name: ")
                result = pokemon_df[pokemon_df['identifier'].str.lower() == pokemon_name.lower()]
                
                if result.empty:
                    print("This mysterious Pokemon cannot be found.")
                else:
                    print(result[['identifier', 'id', 'height', 'weight']])
            
            elif choice == '2':
                region_name = input("Enter a region name: ")
                region = regions_df[regions_df['identifier'].str.lower() == region_name.lower()]
                
                if region.empty:
                    print("This region does not exist.")
                else:
                    region_id = region['id'].values[0]
                    locations = locations_df[locations_df['region_id'] == region_id][['identifier']]
                    print(locations)
            
            elif choice == '3':
                print("Goodbye, Ash!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error reading file: {e}")

main_menu('poke.csv', 'regions.csv', 'locations-2.csv')
