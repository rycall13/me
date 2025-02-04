import pandas as pd

def summarize_pokemon_data(file_path):
    try:
        df = pd.read_csv(file_path)
        

        num_columns = df.shape[1]
        num_rows = df.shape[0]
        

        column_names = list(df.columns)
        

        print(f"The pokemon dataset consists of {num_columns} columns and {num_rows} rows.")
        print(f"It has the following column names: {column_names}")
    except Exception as e:
        print(f"Error reading file: {e}")


summarize_pokemon_data('poke.csv')
