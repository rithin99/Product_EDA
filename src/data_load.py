import pandas as pd

# Function to load dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to describe dataset and save to file
def describe_dataset(df, name, file):
    file.write(f"\n Dataset: {name}\n")
    file.write("-" * 50 + "\n")
    file.write("\n Column Info:\n")
    file.write(str(df.info(buf=file)) + "\n")  # Show column types and missing values
    file.write("\n First 5 Rows:\n")
    file.write(str(df.head()) + "\n")  # Show first few rows
    file.write("\n Summary Statistics:\n")
    file.write(str(df.describe()) + "\n")  # Show numerical summary