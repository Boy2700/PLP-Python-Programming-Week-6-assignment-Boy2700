# Filename: generate_dataset.py

import pandas as pd
import numpy as np

# Define a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data similar to the Iris dataset
n_samples = 150

data = {
    "sepal_length": np.random.normal(loc=5.8, scale=0.8, size=n_samples),
    "sepal_width": np.random.normal(loc=3.0, scale=0.4, size=n_samples),
    "petal_length": np.random.normal(loc=4.3, scale=1.3, size=n_samples),
    "petal_width": np.random.normal(loc=1.3, scale=0.4, size=n_samples),
    "species": np.random.choice(["setosa", "versicolor", "virginica"], size=n_samples)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("synthetic_data.csv", index=False)
print("Dataset 'synthetic_data.csv' generated successfully.")
