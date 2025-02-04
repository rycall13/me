import pandas as pd

def count_locations_by_region(regions_file, locations_file):
    try:
        regions_df = pd.read_csv(regions_file)
        locations_df = pd.read_csv(locations_file)
        
        while True:
            region_name = input("Enter a region name (or type 'exit' to quit): ")
            
            if region_name.lower() == 'exit':
                print("Exiting...")
                break
            
            region = regions_df[regions_df['identifier'].str.lower() == region_name.lower()]
            
            if region.empty:
                print("This region does not exist")
            else:
                region_id = region['identifier'].values[0]
                location_count = locations_df[locations_df['region_id'] == region_id].shape[0]
                print(f"Number of locations in {region_name}: {location_count}")

        unassociated_locations = locations_df[locations_df['region_id'].isna()]
        print("Locations not associated with any region:")
        print(unassociated_locations)
    except Exception as e:
        print(f"Error reading file: {e}")

count_locations_by_region('regions.csv', 'locations-2.csv')
