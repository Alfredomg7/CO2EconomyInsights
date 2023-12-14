# CO2EconomyInsights
## Introduction
Welcome to CO2EconomyInsights! This project is an in-depth analysis aimed at uncovering the intricate relationships between CO2 emissions, economic activity, population growth, and temperature variations. Climate change, marked significantly by increasing CO2 emissions, is one of the most pressing issues humanity faces today. Our focus is on data spanning from 1990 to 2020, delving into the contributing factors, the varying roles of different countries and regions, and the overarching trends that define this critical period in environmental change.

We believe that understanding the dynamics of CO2 emissions is essential to formulating effective policies, raising awareness, and driving action to mitigate the impacts of climate change. This project strives to bring clarity to these dynamics, offering insights that are accessible, comprehensible, and actionable.

## Objective
The primary objective of this project is to analyze the trends and correlations between CO2 emissions and economic (GDP), demographic (population), and environmental (temperature) factors across different countries and regions from 1990 to 2020. The analysis aims to identify the leading contributors to CO2 emissions, understand the influence of economic growth and population size on emissions, and observe the impact of rising temperatures, providing insights for targeted climate action.

## Questions to Answer:
1. **Global CO2 Emissions Trends** (1990-2020):
- **Chart**: Line graph showing the global yearly CO2 emissions over time.
- **Purpose**: Visualize the overall trend of CO2 emissions globally, identifying periods of increase or decrease.
2. **Geographical Distribution and Top Contributors to CO2 Emissions**:
- **Chart**:  Interactive global map visualizing total CO2 emissions by country from 1990 to 2020 and a bar chart showing top contributors' emissions with compacted data points.
- **Purpose**: Identify major contributors to global CO2 emissions. The interactive map provides a global overview, while the bar chart highlights the top 10 contributors.
3. **Correlation Between GDP, Population and, CO2 Emissions**:
- **Chart**: Bubble chart where the size of each bubble represents a country's population, placed on a grid of CO2 emissions versus GDP.
- **Purpose**: Investigate if countries with larger economies or populations tend to have higher emissions, and if economic growth and population size correlate with emission increases.
4. **Emissions per Capita vs GDP**:
- **Chart**: Scatter plot analyzing the relationship between CO2 emissions per capita and GDP, highlighting how economic growth relates to emissions on a per-person basis.
- **Purpose**: Explore if higher economic output (GDP) correlates with higher or lower CO2 emissions per capita, providing insights into how economic development impacts environmental sustainability on an individual level.
5. **Temperature Changes Alongside CO2 Emissions**:
- **Chart**: Dual-axis line chart with yearly average temperatures and CO2 emissions over time.
- **Purpose**: Explore potential correlations between rising temperatures and increasing CO2 emissions, providing insights into climate change dynamics.

## Get Started
### Prerequisites
Ensure you have Python (preferably Python 3.10) and Git installed on your system. You will also need specific libraries for data processing and visualization. Install them using:
`pip install pandas plotly`
## Steps
### 1. Clone the Repository:
clone the repository to your local machine using:
`git clone https://github.com/Alfredomg7/CO2EconomyInsights`

### 2. Data Cleaning:
- Navigate to the directory containing the `clean_data.py` script.
- Run the script to clean and preprocess the datasets. This generates cleaned versions of the data required for analysis.
`python clean_data.py`

### 3. Running the Main Analysis:
- After cleaning the data, navigate to the directory containing the `main_analysis` module.
- Execute the module to create the Plotly charts for the analysis.
`python main_analysis.py`

## Notes:
- Ensure all datasets are correctly placed in the designated data directory as referenced in the scripts.
- You need internet access while running the scripts, as some libraries may fetch additional data or resources online.
- The results will be displayed directly in your Python environment or can be exported as HTML files for easy sharing and viewing.