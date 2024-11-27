import pandas as pd

file_path = "customers.csv"  # Ensure this matches your file name
data = pd.read_csv(file_path)


print("First 5 rows of the dataset:")
print(data.head())


print("\nDataset Information:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

print("last 5 rows of the dataset:")
print(data.tail())
