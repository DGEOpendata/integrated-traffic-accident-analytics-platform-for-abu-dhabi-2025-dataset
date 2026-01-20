python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Abu Dhabi Traffic Accident Dataset 2025
file_path = 'Traffic_Accident_Abu_Dhabi_2025.xlsx'
data = pd.read_excel(file_path)

# Basic exploration
print(data.head())
print(data.info())

# Create a heatmap for accident hotspots
def generate_heatmap(data, city_column, street_column):
    grouped_data = data.groupby([city_column, street_column]).size().reset_index(name='accident_count')
    pivot_table = grouped_data.pivot(city_column, street_column, 'accident_count')
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", cbar=True)
    plt.title('Traffic Accident Hotspots - 2025')
    plt.xlabel('Streets')
    plt.ylabel('Cities')
    plt.show()

# Generate heatmap using the function
generate_heatmap(data, 'City', 'Street')

# Correlation analysis between weather and accidents
def correlation_analysis(data, weather_column, accident_count_column):
    correlation = data[[weather_column, accident_count_column]].corr()
    print("Correlation between Weather and Accident Counts:")
    print(correlation)

# Perform correlation analysis
correlation_analysis(data, 'Weather Condition', 'Number of Accidents')

# Summary statistics for injuries statistics
def injury_statistics(data, injury_column):
    stats = data[injury_column].describe()
    print("Injury Statistics:")
    print(stats)

# Generate injury statistics
injury_statistics(data, 'Number of Injuries')
