import pandas as pd

# Load the dataset
df = pd.read_csv("sample_missing_data.csv")

# Display original data
print("Original Data:\n", df)

# Fill missing names with "Unknown"
df["Name"] = df["Name"].fillna("Unknown").replace("", "Unknown")
print("\nMissing names filled with 'Unknown':\n", df["Name"])

# Fill missing ages with the mean age
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nMissing ages filled with mean age:\n", df["Age"])

# Fill missing emails with a default value
df["Email"] = df["Email"].fillna("noemail@example.com").replace("", "noemail@example.com")
print("\nMissing emails filled with 'noemail@example.com':\n", df["Email"])

# Fill missing salaries with the median salary
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print("\nMissing salaries filled with median salary:\n", df["Salary"].head())

# Save the cleaned dataset
df.to_csv("cleaned_missing_data.csv", index=False)


# Assignment
# Fill missing values in the "City" column with "Nairobi"
#use dropna() return new values from the data frame

