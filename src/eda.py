import pandas as pd

# Function to convert 'Date' columns to datetime format
def convert_to_datetime(df):
	df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
	return df["Date"]

# Function to fill missing values in columns with 0
def clean_features_data(df):
	markdown_cols = ["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"]
	df[markdown_cols] = df[markdown_cols].fillna(0)
	df["CPI"] = df["CPI"].ffill()	
	df["Unemployment"] = df["Unemployment"].ffill()	
	return df

#Function to Calculate mean, median, and standard deviation for numeric columns of a DataFrame and save it to a text file.
def calculate_and_save_statistics(df, dataset_name, file):
   
    # Calculate statistics

    file.write(f"\n ---- {dataset_name} Statistics ----\n")
    file.write("Mean:\n" + str(df.mean(numeric_only=True)) + "\n")
    file.write("Median:\n" + str(df.median(numeric_only=True)) + "\n")
    file.write("Standard Deviation:\n" + str(df.std(numeric_only=True)) + "\n")



