import requests

# URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Send a GET request to download the dataset
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Write the content of the response (dataset) to a file
    with open("iris.csv", "wb") as file:
        file.write(response.content)
    print("Dataset downloaded successfully as iris.csv")
else:
    print("Failed to download dataset")

import pandas as pd

# Load the Iris dataset (assuming it's in CSV format and named iris.csv)
iris_df = pd.read_csv("iris.csv", header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

# Calculate summary statistics for each variable
summary_stats = iris_df.describe()

# Convert the summary statistics DataFrame to a string
summary_stats_str = summary_stats.to_string()

# Define the file path for the output text file
output_file_path = "summary_stats.txt"

# Write the summary statistics to the output text file
with open(output_file_path, "w") as file:
    file.write(summary_stats_str)

print(f"Summary statistics saved to {output_file_path}")

import matplotlib.pyplot as plt

# Load the Iris dataset (assuming it's in CSV format and named iris.csv)
iris_df = pd.read_csv("iris.csv", header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

# Create histograms for each variable
for column in iris_df.columns[:-1]:  # Exclude the 'species' column
    plt.figure()  # Create a new figure
    plt.hist(iris_df[column], bins=10, color='skyblue', edgecolor='black')  # Create histogram
    plt.title(f'Histogram of {column}')  # Set title
    plt.xlabel(column)  # Set x-axis label
    plt.ylabel('Frequency')  # Set y-axis label
    plt.grid(True)  # Show grid
    plt.tight_layout()  # Adjust layout
    plt.savefig(f'{column}_histogram.png')  # Save histogram as PNG file
    plt.close()  # Close the current figure to release memory

print("Histograms saved as PNG files.")

# Create scatter plots for each pair of variables
for i, col1 in enumerate(iris_df.columns[:-1]):
    for col2 in iris_df.columns[i+1:]:
        plt.figure()  # Create a new figure
        plt.scatter(iris_df[col1], iris_df[col2], c='blue', alpha=0.5)  # Create scatter plot
        plt.title(f'Scatter plot of {col1} vs {col2}')  # Set title
        plt.xlabel(col1)  # Set x-axis label
        plt.ylabel(col2)  # Set y-axis label
        plt.grid(True)  # Show grid
        plt.tight_layout()  # Adjust layout
        plt.savefig(f'{col1}_vs_{col2}_scatter.png')  # Save scatter plot as PNG file
        plt.close()  # Close the current figure to release memory

print("Scatter plots saved as PNG files.")
