import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
file_2025 = '/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/demand_2025_iberian-peninsula.csv'
#file_2003 = os.path.join('cy_stress-test', '/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/cy_stress-test/demand_2025_iberian-peninsula.csv')
file_2003 = '/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/demand_2025_iberian-peninsula.csv'

# Function to load and process the data
def load_and_process(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Split the single column into separate columns
    data[['climatic_year', 'date', 'value']] = data['climatic_year;date;value'].str.split(';', expand=True)
    
    # Drop the original combined column
    data = data.drop(columns=['climatic_year;date;value'])
    
    # Convert 'date' to datetime and 'value' to numeric for processing
    data['date'] = pd.to_datetime(data['date'])
    data['value'] = pd.to_numeric(data['value'])
    
    # Group by hour of the day to compute the average value across all years
    data['hour'] = data['date'].dt.hour
    hourly_avg = data.groupby('hour')['value'].mean()
    
    # Create a new DataFrame for a single "averaged" day
    averaged_day = pd.DataFrame({
        'hour': hourly_avg.index,
        'average': hourly_avg.values
    })
    
    # Expand this to include timestamps for plotting
    averaged_day['date'] = pd.date_range(start='1900-01-01', periods=24, freq='H')
    averaged_day.set_index('date', inplace=True)
    print(averaged_day.max())
    # Calculate daily max, min, and average
    averaged_day['daily_max'] = averaged_day['average'].resample('D').transform('max')
    averaged_day['daily_min'] = averaged_day['average'].resample('D').transform('min')
    
    return averaged_day

# Process both datasets
averaged_day_2025 = load_and_process(file_2025)
averaged_day_2003 = load_and_process(file_2003)

# Plot comparison for 2025 and 2003
plt.figure(figsize=(14, 8))
# Plot for 2025
plt.plot(averaged_day_2025.index, averaged_day_2025['average'], label='2025 Hourly Average', color='blue')
plt.plot(averaged_day_2025.index, averaged_day_2025['daily_max'], label='2025 Daily Max', color='skyblue', linestyle='--')
plt.plot(averaged_day_2025.index, averaged_day_2025['daily_min'], label='2025 Daily Min', color='lightblue', linestyle=':')

# Plot for 2003
plt.plot(averaged_day_2003.index, averaged_day_2003['average'], label='2003 Hourly Average', color='red')
plt.plot(averaged_day_2003.index, averaged_day_2003['daily_max'], label='2003 Daily Max', color='orange', linestyle='--')
plt.plot(averaged_day_2003.index, averaged_day_2003['daily_min'], label='2003 Daily Min', color='salmon', linestyle=':')

# Add legend, title, and labels
plt.legend()
plt.title('Hourly Demand: Daily Max, Min, and Average for 2025 and 2003')
plt.xlabel('Time (Hours)')
plt.ylabel('Demand')
plt.grid(True)
plt.tight_layout()

# Save the comparison plot
output_path_comparison = 'demand_comparison_2025_vs_2003.png'
plt.savefig(output_path_comparison)
plt.close()

print(f"Comparison plot saved as {output_path_comparison}")

# Load and process 2003 dataset
file_2003 = os.path.join('cy_stress-test', '/workspaces/planning-the-european-electric-system-europe-1/data/ERAA_2023-2/demand/cy_stress-test/demand_2025_iberian-peninsula.csv')

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
