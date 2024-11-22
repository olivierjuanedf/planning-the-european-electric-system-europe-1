import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the year as a variable
country = "poland"
target_year = 2025
climatic_year = 2003
window_size = 24 * 7  # Sliding average window size in hours (adjust as needed)

os.makedirs('out', exist_ok=True)

# Read the data from the CSV file, using ';' as the separator
# data = pd.read_csv(f'data/ERAA_2023-2/demand/demand_{target_year}_{country}.csv', sep=';')
data = pd.read_csv(f'/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/demand_2025_{country}.csv', sep=';')
#############################################
# If the year which you want to test is not in the above path for the csv file then try the below path:
# data = pd.read_csv(f'/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/cy_stress-test/demand_2025_{country}.csv', sep=';')

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Filter data for the climatic_year
data_target_year = data[data['climatic_year'] == climatic_year]

# Check if data is available for the target year
if data_target_year.empty:
    print(f"No data available for the year {climatic_year}.")
else:
    # Calculate the sliding average
    data_target_year['sliding_avg'] = data_target_year['value'].rolling(window=window_size).mean()

    # Plot the original data
    plt.figure(figsize=(12, 6))
    plt.plot(data_target_year['date'], data_target_year['value'], linestyle='-', label='Original Data')

    # Plot the sliding average
    plt.plot(data_target_year['date'], data_target_year['sliding_avg'], color='red', linestyle='-', label=f'{window_size}-Hour Sliding Average')

    # Add labels and title
    plt.xlabel(f'Date ({climatic_year})')
    plt.ylabel('Value')
    # plt.ylim(30000, 100000)
    plt.title(f'Values for {climatic_year} with Sliding Average')
    plt.grid(True)

    # Add legend
    plt.legend()

    # Format x-axis ticks dynamically based on the target year dates
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"out/demand_{target_year}_climatic-{climatic_year}_sca")
