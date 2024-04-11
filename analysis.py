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
