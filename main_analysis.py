import pandas as pd
import plotly.express as px

# Load cleaned datasets
path = "data/clean_data/"
co2_data = pd.read_csv(f"{path}cleaned_co2_data.csv")
gdp_data = pd.read_csv(f"{path}cleaned_gdp_data.csv")
pop_data = pd.read_csv(f"{path}cleaned_pop_data.csv")
temp_data = pd.read_csv(f"{path}cleaned_temp_data.csv")
country_data = pd.read_csv(f"{path}cleaned_country_data.csv")

"""Global CO2 emissions trends"""
annual_global_emissions = co2_data.groupby("Year")["CO2 Emissions"].sum().reset_index()

# Create a line graph showing the global yearly CO2 emissions over time
fig = px.line(annual_global_emissions, 
              x='Year', 
              y='CO2 Emissions', 
              title='Global CO2 Emissions Trend (1990-2020)',
              labels={'Total CO2 Emissions': 'Total CO2 Emissions (metric tons)',
                      'Year': 'Year'},
              line_shape='linear')

# Customizing line color and adding markers
fig.update_traces(line=dict(color='#b30000', width=2), mode='lines+markers')

# Show plot
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

# Hide color legend for better readibility
fig.update_layout(coloraxis_showscale=False)

# Show the visualization
fig.show()

# Identify the top 10 emitting countries over the entire period
top_emitters = co2_data.groupby('Country Name')['CO2 Emissions'].sum().nlargest(10).reset_index()

# Create the bar chart visualization for the sum of CO2 emissions from 1990 to 2020
fig = px.bar(top_emitters,
             x='Country Name',
             y='CO2 Emissions',
             color="CO2 Emissions",
             color_continuous_scale=px.colors.diverging.RdBu_r,
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

"""Correlation Between GDP and CO2 Emissions"""

# Sum the CO2 emissions and GDP for each country over all years
co2_total = co2_data.groupby('Country Code')['CO2 Emissions'].sum().reset_index()
gdp_total = gdp_data.groupby('Country Code')['GDP'].sum().reset_index()

# Merge the totals on 'Country Code'
co2_gdp_data = pd.merge(co2_total, gdp_total, on='Country Code')

# Merge the 'country_data' dataset to add 'Region' and 'Income Group'
co2_gdp_data = pd.merge(co2_gdp_data, country_data, on='Country Code')

# Create the scatter plot
fig = px.scatter(co2_gdp_data,      
                 x='GDP', 
                 y='CO2 Emissions',
                 hover_name='Country Name',
                 title='Total GDP vs Total CO2 Emissions (1990-2020)',
                 color='IncomeGroup',
                 log_x=True,
                 log_y=True)

# Customize the layout
fig.update_layout(
    xaxis_title="Total GDP (in USD - log scale)",
    yaxis_title="Total CO2 Emissions (in metric tons - log scale)",
)

# Show the figure
fig.show()

"""Population vs CO2 Emissions"""
# Average the CO2 Emissions and population for each country over all years
co2_mean = co2_data.groupby("Country Code")["CO2 Emissions"].mean().reset_index()
pop_mean = pop_data.groupby("Country Code")["Population"].mean().reset_index()

# Filter out countries with population less than 10M and higher than 250M
min_pop = 10000000
max_pop = 250000000
pop_mean = pop_mean[(pop_mean["Population"] > min_pop) & (pop_mean["Population"] < max_pop)]

# Merge the totals on 'Country Code'
co2_pop_data = pd.merge(pop_mean, co2_mean, on="Country Code")

# Merge with 'country data'
co2_pop_data = pd.merge(co2_pop_data, country_data, on="Country Code")

# Create the buble chart
fig = px.scatter(co2_pop_data,
                 x="Population",
                 y="CO2 Emissions",
                 hover_name="Country Name",
                 title="Population vs CO2 Emissions (1990-2020)",
                 size="Population",
                 color="Region",
                 log_x=True,
                 log_y=True
                )

# Customize the layout
fig.update_layout(
    xaxis_title="Average Population (log scale)",
    yaxis_title="Total CO2 Emissions (in metric tons - log scale)",
)

# Show the chart
fig.show()
