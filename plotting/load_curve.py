import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the year as a variable
country = "germany"
target_year = 2025
climatic_year1 = 1987
climatic_year2 = 2003

os.makedirs('out', exist_ok=True)

# Read the data from the CSV files, using ';' as the separator
data1 = pd.read_csv('/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/cy_stress-test/demand_2025_germany.csv', sep=';')
data2 = pd.read_csv('/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/demand_2025_germany.csv', sep=';')

# Convert 'date' column to datetime format
data1['date'] = pd.to_datetime(data1['date'])
data2['date'] = pd.to_datetime(data2['date'])

# Filter data for the climatic_year
data_target_year1 = data1[data1['climatic_year'] == climatic_year1]
data_target_year2 = data2[data2['climatic_year'] == climatic_year2]

# Check if data is available for both climatic years
if data_target_year1.empty:
    print(f"No data available for the climatic year {climatic_year1}.")
if data_target_year2.empty:
    print(f"No data available for the climatic year {climatic_year2}.")

if not data_target_year1.empty and not data_target_year2.empty:
    # Sort the demand values in descending order
    sorted_values1 = data_target_year1['value'].sort_values(ascending=False).reset_index(drop=True)
    sorted_values2 = data_target_year2['value'].sort_values(ascending=False).reset_index(drop=True)

    # Calculate the exceedance probability for both datasets
    exceedance_prob1 = (sorted_values1.index + 1) / len(sorted_values1) * 100
    exceedance_prob2 = (sorted_values2.index + 1) / len(sorted_values2) * 100

    # Plot the load duration curves
    plt.figure(figsize=(12, 6))
    plt.plot(exceedance_prob1, sorted_values1, linestyle='-', color='blue', label=f'Load Duration Curve {climatic_year1}')
    plt.plot(exceedance_prob2, sorted_values2, linestyle='-', color='green', label=f'Load Duration Curve {climatic_year2}')
    
    # Add labels, title, and legend
    plt.xlabel('Exceedance Probability (%)')
    plt.ylabel('Demand Value')
    plt.title(f'Load Duration Curves for {climatic_year1} and {climatic_year2}')
    plt.ylim(30000, 90000)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"out/load_duration_curve_{target_year}_climatic-{climatic_year1}-{climatic_year2}.png")
else:
    print("Insufficient data to plot load duration curves.")
