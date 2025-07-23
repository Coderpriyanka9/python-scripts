import pandas as pd

# Sample CSV read
df = pd.read_csv('employees.csv')

# Preview data
print(df.head())

# Drop rows with missing names
df = df.dropna(subset=['Name'])

# Fill missing salaries with the mean
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Fix data types
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# Remove duplicates
df = df.drop_duplicates()

# Export cleaned data
df.to_csv('cleaned_employees.csv', index=False)
