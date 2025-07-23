import pandas as pd

# Sample employee data
data = {
    'Name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'Salary': [70000, 80000, 60000, None, 75000],
    'JoinDate': ['2022-01-15', '2021-03-10', '2020-07-25', '2023-06-01', '2022-11-20']
}

# Create a DataFrame
df_sample = pd.DataFrame(data)

# Save it as employees.csv
df_sample.to_csv('employees.csv', index=False)

print("Sample 'employees.csv' created.")
