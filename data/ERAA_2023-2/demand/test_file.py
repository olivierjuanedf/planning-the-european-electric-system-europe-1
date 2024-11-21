import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def load_file(folder, file_name):
    """
    Load the CSV file based on the folder and file name.
    """
    file_path = os.path.join(folder, file_name)
    try:
        data = pd.read_csv(file_path, sep=";")
        print(f"Loaded file: {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def process_origin_file(df_origin):
    """
    Process the Origin file to compute an average year baseline (daily stats).
    """
    # Convert 'date' column to datetime and extract day-of-year and year
    df_origin['date'] = pd.to_datetime(df_origin['date'])
    df_origin['day_of_year'] = df_origin['date'].dt.dayofyear
    df_origin['year'] = df_origin['date'].dt.year

    # Group by day_of_year for each year, then compute daily statistics
    daily_stats_by_year = df_origin.groupby(['year', 'day_of_year'])['value'].agg(['max', 'min', 'mean']).reset_index()

    # Average the daily stats across all years to get the baseline
    average_year_baseline = daily_stats_by_year.groupby('day_of_year').mean().reset_index()
    return average_year_baseline

def process_cv_file(df_cv, climatic_year):
    """
    Process the CV file to compute daily stats for a specific climatic year.
    """
    # Convert 'date' column to datetime and filter by the specified climatic year
    df_cv['date'] = pd.to_datetime(df_cv['date'])
    df_cv = df_cv[df_cv['climatic_year'] == climatic_year]

    # Extract day-of-year and compute daily statistics
    df_cv['day_of_year'] = df_cv['date'].dt.dayofyear
    daily_stats_cv = df_cv.groupby('day_of_year')['value'].agg(['max', 'min', 'mean']).reset_index()
    return daily_stats_cv

def plot_comparison(average_year_baseline, daily_stats_cv, climatic_year, country):
    """
    Plot separate comparisons for minimum, average, and maximum values.
    """

    def save_plot(y_baseline, y_cv, ylabel, title, output_file, color_baseline, color_cv):
        """
        Helper function to create and save individual plots.
        """
        plt.figure(figsize=(14, 8))
        plt.plot(average_year_baseline['day_of_year'], y_baseline, label='Baseline (Origin)', color=color_baseline, linewidth=1)
        plt.plot(daily_stats_cv['day_of_year'], y_cv, label=f"CV (Year {climatic_year})", color=color_cv, linewidth=1)

        # Formatting the graph
        plt.title(title)
        plt.xlabel("Day of the Year")
        plt.ylabel(ylabel)
        plt.grid(True, alpha=0.5)
        plt.legend()

        # Save the plot
        plt.savefig(output_file)
        print(f"Saved plot as '{output_file}'")
        plt.close()

    # Minimum plot
    save_plot(
        y_baseline=average_year_baseline['min'],
        y_cv=daily_stats_cv['min'],
        ylabel="Minimum Demand",
        title=f"Minimum Daily Demand Comparison for {country.capitalize()} (Baseline vs Year {climatic_year})",
        output_file=f"demand_min_comparison_{country}year{climatic_year}.png",
        color_baseline="cyan",
        color_cv="orange"
    )

    # Average plot
    save_plot(
        y_baseline=average_year_baseline['mean'],
        y_cv=daily_stats_cv['mean'],
        ylabel="Average Demand",
        title=f"Average Daily Demand Comparison for {country.capitalize()} (Baseline vs Year {climatic_year})",
        output_file=f"demand_avg_comparison_{country}year{climatic_year}.png",
        color_baseline="navy",
        color_cv="brown"
    )

    # Maximum plot
    save_plot(
        y_baseline=average_year_baseline['max'],
        y_cv=daily_stats_cv['max'],
        ylabel="Maximum Demand",
        title=f"Maximum Daily Demand Comparison for {country.capitalize()} (Baseline vs Year {climatic_year})",
        output_file=f"demand_max_comparison_{country}year{climatic_year}.png",
        color_baseline="blue",
        color_cv="red"
    )


    # Ensure the country name and climatic year are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script_name.py <country_name> <climatic_year>")
    sys.exit(1)

country = sys.argv[1].lower()  # Get the country name from command-line arguments
climatic_year = int(sys.argv[2])  # Get the climatic year to analyze from command-line arguments
folder_cv = "cv_stress-test"  # Folder containing the CV file
folder_origin = "."  # Current folder containing the Origin file

    # Load the files
origin_file_name = f"demand_2025_{country}.csv"  # Assuming the Origin file is named similarly
cv_file_name = f"demand_2025_{country}.csv"  # Assuming the CV file is named similarly

df_origin = load_file(folder_origin, origin_file_name)


df_cv = load_file(folder_cv, cv_file_name)

    # Process the Origin file to compute the average year baseline
average_year_baseline = process_origin_file(df_origin)

    # Process the CV file to compute daily stats for the selected climatic year
daily_stats_cv = process_cv_file(df_cv, climatic_year)

    # Plot separate comparisons
plot_comparison(average_year_baseline, daily_stats_cv, climatic_year, country)

