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

