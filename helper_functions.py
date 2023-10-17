import pandas as pd

def inspect_data(data):
    print(data.head(10))
    print(data.info())
    print("-"*220)  

    return None

def clean_indicators_data(data):
    columns_to_keep = ["Country Name", "Country Code"] + [str(year) for year in range(1990, 2021)]
    clean_data = data[columns_to_keep]
    clean_data = clean_data.dropna(subset=[str(year) for year in range(1990,2021)], how='all')

    return clean_data

def clean_country_data(data):
    clean_data = data.drop(columns=["SpecialNotes"])
    clean_data.rename(columns={"TableName":"Country Name"}, inplace=True)
    cols = ["Country Name"] + [col for col in clean_data if col!= "Country Name"]
    clean_data = clean_data[cols]
    
    return clean_data

def clean_temperature_data(data):
    # Preprocessing and filtering data
    data["dt"] = pd.to_datetime(data["dt"])
    data["Year"] = data["dt"].dt.year
    data = data[data["Year"].between(1990,2020)]

    # Grouping and aggregating data
    annual_data = data.groupby(["Year","Country"])["AverageTemperature"].mean().reset_index()
    # Pivoting data
    pivot_data = annual_data.pivot(index="Country", columns="Year", values="AverageTemperature").reset_index()
    
    # Adding and ordering columns
    pivot_data["Country Code"] = ""
    pivot_data = pivot_data[['Country', 'Country Code'] + [col for col in pivot_data if col not in ['Country', 'Country Code']]] 

    # Renaming columns
    pivot_data.columns = ['Country Name', 'Country Code'] + [str(col) for col in pivot_data.columns[2:]]

    return pivot_data

