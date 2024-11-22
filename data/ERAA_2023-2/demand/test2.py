import pandas as pd
import matplotlib.pyplot as plt

# Define file path for the original dataset
file_2003 = '/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/demand_2025_iberian-peninsula.csv'

# Load and process 2003 dataset for sorted line graph
data = pd.read_csv(file_2003)

# Split and process
data[['climatic_year', 'date', 'value']] = data['climatic_year;date;value'].str.split(';', expand=True)
data = data.drop(columns=['climatic_year;date;value'])
data['date'] = pd.to_datetime(data['date'])
data['value'] = pd.to_numeric(data['value'])

# Debug: Check climatic_year values
print(f"Unique climatic years in the dataset: {data['climatic_year'].unique()}")

# Filter for 2003 based on climatic_year
data_2003 = data[data['climatic_year'] == '2003']

# Debug: Check filtering
print(f"Number of rows for climatic year 2003: {data_2003.shape[0]}")
print(f"2003 data preview:\n{data_2003.head()}")

# Sort values from high to low
sorted_values = data_2003['value'].sort_values(ascending=False).reset_index(drop=True)

# Debug: Check sorted values
print(f"First few sorted values:\n{sorted_values.head()}")
print(f"Total values in sorted series: {sorted_values.shape[0]}")

# Plot sorted line graph
plt.figure(figsize=(14, 8))
plt.plot(sorted_values, label='2003 Hourly Demand (Sorted)', color='green')

# Add legend, title, and labels
plt.legend()
plt.title('Hourly Demand (2003): Sorted High to Low')
plt.xlabel('Hour Rank (High to Low)')
plt.ylabel('Demand')
plt.grid(True)
plt.tight_layout()

# Save the sorted line graph
output_path_sorted = 'sorted_hourly_demand_2003.png'
plt.savefig(output_path_sorted)
plt.close()

print(f"Sorted demand plot saved as {output_path_sorted}")

print("COMPARE")
print("Sample hourly averages across all years:")
print(averaged_day_2025['average'].head())

print("Sample hourly values for 2003:")
print(data_2003.groupby(data_2003['date'].dt.hour)['value'].mean().head())
