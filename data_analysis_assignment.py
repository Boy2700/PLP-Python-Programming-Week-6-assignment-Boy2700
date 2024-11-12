# Filename: data_analysis_assignment.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    data = pd.read_csv("synthetic_data.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("File not found. Please ensure 'synthetic_data.csv' is in the same directory.")

# Display the first few rows
print("First few rows of the dataset:")
print(data.head())

# Check the structure of the dataset
print("\nData Types and Missing Values:")
print(data.info())

# Check for missing values
print("\nMissing Values per Column:")
print(data.isnull().sum())

# Handle any missing values if any (here we'll fill with mean as an example)
if data.isnull().values.any():
    data.fillna(data.mean(), inplace=True)
    print("\nMissing values have been filled.")
else:
    print("\nNo missing values found.")

# Basic statistics
print("\nBasic Statistics of Numerical Columns:")
print(data.describe())

# Group by species and compute the mean of numerical columns
print("\nMean of Numerical Columns Grouped by Species:")
species_mean = data.groupby("species").mean()
print(species_mean)

# Observations
print("\nObservations:")
print("- Mean values vary significantly across species, similar to the Iris dataset.")
print("- This may indicate differing physical characteristics among the species.")

# Visualization Section

# Line chart of Sepal and Petal Length over the sample index (simulated time trend)
data['index'] = data.index
plt.figure(figsize=(10, 6))
plt.plot(data['index'], data['sepal_length'], label='Sepal Length')
plt.plot(data['index'], data['petal_length'], label='Petal Length')
plt.title('Trends in Sepal and Petal Length')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.show()

# Bar chart for average sepal width per species
plt.figure(figsize=(8, 6))
species_mean['sepal_width'].plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Average Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Width (cm)')
plt.show()

# Histogram of Petal Length
plt.figure(figsize=(8, 6))
plt.hist(data['petal_length'], bins=20, color='purple', alpha=0.7)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Sepal Length vs Petal Length by Species
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
