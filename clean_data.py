""" Data Preparation """
import pandas as pd
from helper_functions import *

# File names and their respective indicators
files_and_indicators = {
    "co2_data": "CO2 Emissions",
    "gdp_data": "GDP",
    "pop_data": "Population",
    "country_data": None,
    "temp_data": None
}

# Base path
path = "data/raw_data/"

# Load and inspect datasets
datasets = {}
for filename in files_and_indicators.keys():
    
    # Load dataset
    data = pd.read_csv(f"{path}{filename}.csv")
    
    # Store dataset in the dictionary
    datasets[filename] = data

    # Inspect raw data
    print(f"Inspecting {filename}:")
    inspect_data(data)

# Get a list of valid countries from the country_data
valid_countries = get_valid_country_codes(datasets["country_data"])

""" Data Cleaning """
cleaned_datasets = {}
for filename, indicator_name in files_and_indicators.items():
    
    data = datasets[filename]
    cleaned_data = None

    if indicator_name is not None:
        cleaned_data = clean_indicators_data(data, valid_countries, indicator_name)
    
    elif filename == "temp_data":
        cleaned_data = clean_temperature_data(data,cleaned_datasets["co2_data"])
        
    elif filename == "country_data":
        cleaned_data = clean_country_data(data, valid_countries)

    # Store cleaned data in the dictionary
    cleaned_datasets[filename] = cleaned_data

    # Inspect cleaned data
    print(f"Inspecting cleaned {filename}:")
    inspect_data(cleaned_data)

    # Save cleaned data to a new CSV file
    cleaned_data.to_csv(f"data/clean_data/cleaned_{filename}.csv", index=False)




