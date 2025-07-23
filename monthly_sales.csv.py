import pandas as pd

# Sample employee data
data = {
    'Date': ['2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25'],
    'Product': ['Maggie', 'Momos', 'Pizzas', 'Biryani'],
    'Amount': [100, 150 , 300 , 250]
}
# Create a DataFrame
df_sample = pd.DataFrame(data)

# Save it as employees.csv
df_sample.to_csv('monthly_sales.csv', index=False)

print("Sample 'monthly_sales.csv' created.")
