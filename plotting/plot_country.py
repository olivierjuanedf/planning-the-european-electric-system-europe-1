import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the 'out' directory if it doesn't exist
os.makedirs('out/country', exist_ok=True)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('/workspaces/planning-the-european-electric-system-europe-1/output/long_term_uc/data/opt_power_europe_2025_cy1989_1900-01-01.csv')

# Convert the 'snapshot' column to datetime
df['snapshot'] = pd.to_datetime(df['snapshot'])

# Set the 'snapshot' column as the index
df.set_index('snapshot', inplace=True)

# Get a set of all country codes in the dataset
country_codes = set(col.split('_')[0] for col in df.columns if '_' in col)

# Loop over each country and plot their energy production types
for country_code in country_codes:
    # Extract all columns that start with the current country code
    country_columns = [col for col in df.columns if col.startswith(country_code + '_')]
    
    # Skip if there are no columns for the country (just in case)
    if not country_columns:
        continue
    
    # Plot each energy production type for the country
    plt.figure(figsize=(12, 6))
    
    for col in country_columns:
        # Extract the energy type from the column name
        energy_type = col.split('_', 1)[1].replace('_', ' ').title()
        plt.plot(df.index, df[col], label=energy_type)
    
    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Energy Production Output')
    plt.title(f'Energy Production Output Over Time for {country_code.upper()}')
    plt.legend(title='Energy Type', loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.grid(True)
    
    # Adjust layout to prevent clipping of legend
    plt.tight_layout()
    
    # Save the plot to 'out/{country_code}.png'
    plt.savefig(f'/workspaces/planning-the-european-electric-system-europe-1/plotting/out/{country_code}.png')
    
    # Close the plot to free up memory
    plt.close()
