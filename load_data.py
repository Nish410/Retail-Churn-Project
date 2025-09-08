import pandas as pd

# The path to your data file (which is now correctly named)
file_path = 'online_retail.csv'

def load_and_inspect_data(path):
    """
    This function loads the CSV data, handles potential encoding errors,
    and prints a summary.
    """
    try:
        print("Attempting to load the dataset...")
        df = pd.read_csv(path, encoding='latin1')
        print("SUCCESS: Dataset loaded successfully!")
        
        print("\n--- 1. First 5 Rows of the Data (df.head()) ---")
        print(df.head())
        
        print("\n--- 2. Data Shape (Rows, Columns) ---")
        print(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
        
        print("\n--- 3. Data Info (Column Names, Data Types, Nulls) ---")
        df.info()

    except FileNotFoundError:
        print(f"ERROR: The file was not found at {path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This block ensures the function runs only when the script is executed directly
if __name__ == "__main__":
    load_and_inspect_data(file_path)