import pandas as pd
import plotly.express as px
from functools import reduce

# Load cleaned datasets
path = "data/clean_data/"
co2_data = pd.read_csv(f"{path}cleaned_co2_data.csv")
gdp_data = pd.read_csv(f"{path}cleaned_gdp_data.csv")
pop_data = pd.read_csv(f"{path}cleaned_pop_data.csv")
temp_data = pd.read_csv(f"{path}cleaned_temp_data.csv")
country_data = pd.read_csv(f"{path}cleaned_country_data.csv")

"""Global CO2 emissions trends"""
# Sum the CO2 emissions for each year 
annual_global_emissions = co2_data.groupby("Year")["CO2 Emissions"].sum().reset_index()

# Create a line chart showing the global yearly CO2 emissions over time
fig = px.line(annual_global_emissions, 
              x="Year", 
              y="CO2 Emissions", 
              title="Global CO2 Emissions Trend (1990-2020)",
              labels={"Total CO2 Emissions": "Total CO2 Emissions (metric tons)",
                      "Year": "Year"},
              line_shape="spline")

# Customizing line color and adding markers
fig.update_traces(line=dict(color='#b30000', width=2), mode='lines+markers')

# Show line chart
fig.show()

""" C02 emissions by Country"""
# Sum CO2 emmissions for each country across all years
country_total_emissions = co2_data.groupby("Country Name")["CO2 Emissions"].sum().reset_index()

# Create an interactive world map of CO2 emissions by country
fig = px.choropleth(country_total_emissions,
                    locations="Country Name",
                    locationmode="country names",
                    color="CO2 Emissions",
                    hover_name="Country Name",
                    color_continuous_scale=px.colors.diverging.RdYlGn_r,
                    title="Total CO2 Emissions by Country (1990-2020)")

# Show the visualization
fig.show()

# Identify the top 10 emitting countries over the entire period
top_emitters = co2_data.groupby('Country Name')['CO2 Emissions'].sum().nlargest(10).reset_index()

# Create the bar chart visualization for the sum of CO2 emissions from 1990 to 2020
fig = px.bar(top_emitters,
             x='Country Name',
             y='CO2 Emissions',
             color="CO2 Emissions",
             color_continuous_scale=px.colors.diverging.RdYlGn_r,
             title='Total CO2 Emissions from 1990 to 2020 for Top 10 Emitting Countries',
             labels={'CO2 Emissions':'Total CO2 Emissions (metric tons)'},
             text='CO2 Emissions')

# Customize the layout for better readability
fig.update_layout(xaxis_tickangle=-45, 
                  yaxis=dict(title='Total CO2 Emissions (metric tons)'),
                  coloraxis_showscale=False)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Show the figure
fig.show()

"""GDP, Population and CO2 correlation"""
# Aggregate GDP, Population and CO2 mean values by year on 'Country Code'
gdp_mean = gdp_data.groupby("Country Code")["GDP"].mean().reset_index()
pop_mean = pop_data.groupby("Country Code")["Population"].mean().reset_index()
co2_mean = co2_data.groupby("Country Code")["CO2 Emissions"].mean().reset_index()

# List of dataframes to merge
dataframes = [gdp_mean, pop_mean, co2_mean, country_data]

# Merge the GDP, Population, CO2 and Country data with reduce
total_data = reduce(lambda left, right: pd.merge(left, right, on='Country Code', suffixes=('', '_right')), dataframes)

# Splitting data between small and big countries based on median population for all countries
median_population = round(total_data["Population"].median()) # Using median value will split the countries evenly
small_countries_data = total_data[total_data["Population"] < median_population]
big_countries_data = total_data[total_data["Population"] >= median_population]

# Define function for create bubble chart
def create_bubble_chart(data, data_label, xaxis_title, yaxis_title, x="GDP", y="CO2 Emissions", size="Population", 
                        color="IncomeGroup", hover_name="Country Name", start_year="1990", end_year="2020", log=True):
    
    fig = px.scatter(data,
                    x=x,
                    y=y,
                    size=size,
                    color=color,
                    hover_name=hover_name,
                    title=f"{x} vs {y} by {size} and {color} from {start_year} to {end_year} ({data_label})",
                    size_max=60,
                    log_x=log,
                    log_y=log
                    )
    
    # Customize the layout
    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title
    )
    # Display chart
    fig.show()

# Create bubble chart for small countries data
data_label = "Small Countries"
xaxis_title = "Average GDP (in USD - log scale)"
yaxis_title = "Average CO2 Emissions (in metric tons - log scale)"
create_bubble_chart(small_countries_data, data_label=data_label, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

# Create bubble chart for big countries data
data_label = "Big Countries"
create_bubble_chart(big_countries_data, data_label=data_label, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

"""GDP vs Emissions per Capita"""
# Create emissions per capita column
total_data["CO2 Emissions per Capita"] = total_data["CO2 Emissions"] / total_data ["Population"]

# Create scatter plot
data_label = "All Countries"
xaxis_title = "Average GDP (in USD)"
yaxis_title = "Average CO2 Emissions per Capita"
y = "CO2 Emissions per Capita"
create_bubble_chart(total_data, data_label=data_label, xaxis_title=xaxis_title, yaxis_title=yaxis_title, y=y, size=None, log=False)