import pandas as pd
import matplotlib.pyplot as plt
import os

# Create the 'out' directory if it doesn't exist
os.makedirs('out/energy_pie_chart', exist_ok=True)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('/workspaces/planning-the-european-electric-system-europe-1/output/long_term_uc/data/opt_power_europe_2025_cy1989_1900-01-01.csv')

# Convert the 'snapshot' column to datetime
df['snapshot'] = pd.to_datetime(df['snapshot'])

# Set the 'snapshot' column as the index
df.set_index('snapshot', inplace=True)

# Get all unique country codes in the dataset
countries = set(col.split('_')[0] for col in df.columns)

# Loop over each country
for country in countries:
    # Extract all columns that start with the current country code
    country_columns = [col for col in df.columns if col.startswith(country + '_')]
    
    # Extract energy types for the country
    energy_types = [col.split('_', 1)[1] for col in country_columns]
    
    # Initialize a dictionary to hold total production per energy type
    total_production = {}
    
    for energy_type in energy_types:
        # Column name for this energy type
        col_name = f'{country}_{energy_type}'
        # Sum over this column to get total production for this energy type
        total_production[energy_type] = df[col_name].sum()
    
    # Convert the dictionary to a pandas Series
    total_production_series = pd.Series(total_production)
    
    # Sort the Series by total production
    total_production_series = total_production_series.sort_values(ascending=False)
    
    # Plot the pie chart
    plt.figure(figsize=(10, 8))
    total_production_series.plot(kind='pie', autopct='%1.1f%%', startangle=140, pctdistance=0.85)
    
    # Draw a circle at the center to make it a donut chart
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    # Customize the plot
    plt.ylabel('')
    plt.title(f'Total Energy Production by Type in {country.upper()}')
    plt.tight_layout()
    
    # Save the plot to 'out/{country}_energy_type_pie_chart.png'
    plt.savefig(f'out/energy_pie_chart/{country}_energy_type_pie_chart.png')
    
    # Close the plot to free up memory
    plt.close()
