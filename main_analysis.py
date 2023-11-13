import pandas as pd
import plotly.express as px

# Load cleaned CO2 data
co2_data = pd.read_csv("data/clean_data/cleaned_co2_data.csv")

# Sum CO2 emissions for each year
annual_global_emissions = co2_data.iloc[:, 2:].sum()

# Convert global emmissions from series to dataframe
annual_global_emissions = pd.DataFrame({"Year": annual_global_emissions.index, "Total CO2 Emissions": annual_global_emissions.values})


# Convert 'Year' from string to integer
annual_global_emissions["Year"] = annual_global_emissions["Year"].astype(int)
print(annual_global_emissions.head(10))

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
fig.show()