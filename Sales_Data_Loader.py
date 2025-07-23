import pandas as pd

# Read sales CSV
sales = pd.read_csv('monthly_sales.csv')

# Convert date column to datetime
sales['Date'] = pd.to_datetime(sales['Date'])

# Total sales per product
total_sales = sales.groupby('Product')['Amount'].sum()
print(total_sales)

# Optional: save to new file
total_sales.to_csv('product_sales_summary.csv')
