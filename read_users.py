import pandas as pd

df = pd.read_json('users.json')

print("First 5 rows of the dataset:")
print(df.head(15))

print("First 5 rows of the dataset:")
print(df.tail())


print("User Details:")
print(df[['name', 'phone']])

# Filter users by a specific email domain
gmail_users = df[df['email'].str.endswith('gmail.com')]
print("\nUsers with Gmail addresses:")
print(gmail_users)

