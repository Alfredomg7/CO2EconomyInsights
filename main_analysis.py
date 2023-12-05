import pandas as pd
import plotly.express as px

# Load cleaned CO2 data
co2_data = pd.read_csv("data/clean_data/cleaned_co2_data.csv")

"""Global CO2 emissions trends"""
# Sum CO2 emissions for each year
annual_global_emissions = co2_data.iloc[:, 2:].sum()

# Convert global emmissions from series to dataframe
annual_global_emissions = pd.DataFrame({"Year": annual_global_emissions.index, "Total CO2 Emissions": annual_global_emissions.values})

# Convert 'Year' from string to integer
annual_global_emissions["Year"] = annual_global_emissions["Year"].astype(int)

# Create a line graph showing the global yearly CO2 emissions over time
fig = px.line(annual_global_emissions, 
              x='Year', 
              y='Total CO2 Emissions', 
              title='Global CO2 Emissions Trend (1990-2020)',
              labels={'Total CO2 Emissions': 'Total CO2 Emissions (metric tons)',
                      'Year': 'Year'},
              line_shape='linear')

# Customizing line color and adding markers
fig.update_traces(line=dict(color='#b30000', width=2), mode='lines+markers')

# Show plot
#fig.show()

""" Top 10 countries with highest C02 emissions """
# Melt the Dataframe to get a 'Year' column
co2_data_melted = co2_data.melt(id_vars=["Country Name", "Country Code"], 
                                var_name="Year", 
                                value_name="CO2 Emissions")

# Convert 'Year' from string to integer
co2_data_melted["Year"] = co2_data_melted["Year"].astype(int)

# Get top 10 countries with highest emmissions in the most recent year's data
latest_year = co2_data_melted["Year"].max()
top_countries = co2_data_melted[co2_data_melted['Year'] == latest_year]\
                    .nlargest(10, 'CO2 Emissions')['Country Name'].tolist()

print(top_countries)