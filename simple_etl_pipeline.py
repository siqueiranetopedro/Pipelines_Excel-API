"""
Simple ETL Pipeline - Extract, Transform, Load
This script extracts data from a CSV file or an API, cleans it, and saves the cleaned data to a new CSV file.
Author: Pedro Siqueira
"""

import pandas as pd  # For working with data
# import requests  # Uncomment this if using API

# OPTION 1: Read from file
file_path = "/Users/pedrosiqueira/Downloads/Motor_Vehicle_Collisions_-_Crashes.csv"  # Change this path
data = pd.read_csv(file_path)  # Load CSV file

# OPTION 2: Read from API (commented out - uncomment to use)
# api_url = "https://api.example.com/data"  # Replace with your API endpoint
# response = requests.get(api_url)  # Get data from API
# data = pd.DataFrame(response.json())  # Convert JSON to DataFrame

print(f"Loaded {len(data)} rows")

# Clean the data
data = data.drop_duplicates()  # Remove duplicates
data = data.fillna(0)  # Fill missing values with 0
print("Data cleaned")

# Save cleaned data
data.to_csv("cleaned_data.csv", index=False)  # Save to new CSV file
print("File saved as cleaned_data.csv")
