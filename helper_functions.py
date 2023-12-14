import pandas as pd
import plotly.express as px
from colors import income_group_colors

def inspect_data(data):
    # Print the first 10 rows of the DataFrame
    print(data.head(10))    
    # Print the info of the DataFrame (column names, counts, data types etc.)
    print(data.info())
    # Print a separator line for better readability
    print("-"*220)

def clean_indicators_data(data, valid_countries, indicator_name):
    # Generate a list of year strings for the required range
    years = [str(year) for year in range(1990, 2021)]
    # Define the columns to be retained in the cleaned data
    columns_to_keep = ["Country Name", "Country Code"] + years
    # Filter the DataFrame to only include the specified columns
    clean_data = data[columns_to_keep]
    # Drop the rows where all year columns have NaN values
    clean_data = clean_data.dropna(subset=years, how='all')
    # Filter to include only valid countries
    clean_data = clean_data[clean_data['Country Code'].isin(valid_countries)]
    # Melt the Dataframe to get a 'Year' column
    clean_data = melt_data(clean_data, indicator_name)

    # Return cleaned Dataframe
    return clean_data

def clean_country_data(data,valid_countries):
    # Drop the 'SpecialNotes' column from the DataFrame
    clean_data = data.drop(columns=["SpecialNotes"])
    # Rename the 'TableName' column to 'Country Name' and 'IncomeGroup' column to 'Income Group'
    clean_data.rename(columns={"TableName":"Country Name", "IncomeGroup":"Income Group"}, inplace=True)
    # Reorder the columns to place 'Country Name' at the first position
    cols = ["Country Name"] + [col for col in clean_data if col!= "Country Name"]
    clean_data = clean_data[cols]
    # Filter to include only valid countries
    clean_data = clean_data[clean_data['Country Code'].isin(valid_countries)]

    # Return cleaned Dataframe
    return clean_data

def clean_temperature_data(data, country_data):
    # Preprocessing and filtering data
    data['Year'] = pd.to_datetime(data['dt']).dt.year
    data = data[data['Year'].between(1990, 2014)]

    # Grouping and aggregating data, then pivoting
    pivot_data = data.groupby(['Year', 'Country'])['AverageTemperature']\
                     .mean().unstack('Year').reset_index()

    # Merging with country_data to get the country codes
    clean_data = pd.merge(pivot_data, country_data[['Country Name', 'Country Code']],
                            left_on='Country', right_on='Country Name', how='left')\
                     .drop(columns='Country')

    # Reordering columns
    cols = ['Country Name', 'Country Code'] + [year for year in range(1990, 2014)]
    clean_data = clean_data[cols]

    # Melt the Dataframe to get a 'Year' column
    clean_data = melt_data(clean_data, "Temperature")

    # Return cleaned Dataframe
    return clean_data

def get_valid_country_codes(country_data, region_column='Region', country_code_column='Country Code'):
    # Get a list of valid countries codes based on the non-null 'Region' column
    valid_countries = country_data[country_data[region_column].notna()]
    return valid_countries[country_code_column].tolist()

def melt_data(data, value_name, id_vars=["Country Name", "Country Code"], var_name="Year"):
    melted_data = data.melt(id_vars=id_vars, var_name=var_name, value_name=value_name)
    return melted_data

# Define function to create bubble chart
def create_bubble_chart(data, data_label, xaxis_title, yaxis_title, x="GDP", y="CO2 Emissions", size=None, 
                        color="Income Group", hover_name="Country Name", start_year="1990", end_year="2020", log=True):
    
    # Adjust the title based on whether a size dimension is provided
    title_suffix = f" by {size} and {color}" if size else f" and {color}"
    full_title = f"{x} vs {y}{title_suffix} from {start_year} to {end_year} ({data_label})"

    # Create the scatter plot
    scatter_kwargs = dict(
        x=x,
        y=y,
        color=color,
        hover_name=hover_name,
        title=full_title,
        log_x=log,
        log_y=log,
        color_discrete_map=income_group_colors
    )
    
    if size:
        scatter_kwargs['size'] = size
        scatter_kwargs['size_max'] = 60

    # Prepare the hover data
    hover_data = {x: ':.2s', y: ':.2s'}
    if size:
        hover_data[size] = ':.2s'
    
    fig = px.scatter(data, **scatter_kwargs, hover_data=hover_data)

    # Customize the layout
    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title
    )
    
    # Display chart
    fig.show()