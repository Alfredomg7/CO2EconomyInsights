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
fig.show()

""" C02 emissions by Country """
# Melt the Dataframe to get a 'Year' column
co2_data_melted = co2_data.melt(id_vars=["Country Name", "Country Code"], 
                                var_name="Year", 
                                value_name="CO2 Emissions")

# Sum CO2 emmissions for each country across all years
country_total_emissions = co2_data_melted.groupby("Country Name")["CO2 Emissions"].sum().reset_index()

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
top_emitters = co2_data_melted.groupby('Country Name')['CO2 Emissions'].sum().nlargest(10).reset_index()

# Create the bar chart visualization for the sum of CO2 emissions from 1990 to 2020
fig = px.bar(top_emitters,
             x='Country Name',
             y='CO2 Emissions',
             title='Total CO2 Emissions from 1990 to 2020 for Top 10 Emitting Countries',
             labels={'CO2 Emissions':'Total CO2 Emissions (metric tons)'},
             text='CO2 Emissions')

# Customize the layout for better readability
fig.update_layout(xaxis_tickangle=-45, 
                  yaxis=dict(title='Total CO2 Emissions (metric tons)'))
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Show the figure
fig.show()