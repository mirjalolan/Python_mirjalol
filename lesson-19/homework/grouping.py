# Group the data by the Category column and calculate the following aggregate statistics 
# for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction

import pandas as pd
sales = pd.read_csv('sales_data.csv')

#1

category_group = sales.groupby('Category')
print(category_group['Quantity'].sum())
print(category_group['Price'].max())
print(category_group['Price'].mean())


#2

top_products = (sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index().sort_values(
    ["Category", "Quantity"], ascending=[True, False]
).drop_duplicates('Category'))

print(top_products)

#3

sales['Sales'] = sales['Quantity'] * sales['Price']
print(sales['Sales'])

sales_date = sales.groupby('Date')['Sales'].sum().reset_index()
best_day = sales_date.loc[sales_date['Sales'].idxmax()]
print(best_day)


orders = pd.read_csv('customer_orders.csv')
# print(orders)

#1
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
order_counts = customer_order = orders.groupby('CustomerID').size()
result = order_counts[order_counts<20]
print(result)

#2
# Identify customers who have ordered products with an average price per unit greater than $120.
avg_price = orders.groupby('CustomerID')['Price'].mean() < 120
print(avg_price[avg_price])

#3
# Find the total quantity and total price for each product ordered, and 
# filter out products that have a total quantity less than 5 units.

quantity_grouped = orders.groupby("Product")["Quantity"].sum()

price_grouped = (orders["Quantity"] * orders["Price"]).groupby(orders["Product"]).sum()

print("Total Quantity per Product:\n", quantity_grouped)
print("\nTotal Sales Value per Product:\n", price_grouped)

quantity_grouped = orders.groupby("Product")["Quantity"].sum()
result = quantity_grouped[quantity_grouped < 5].index
print(orders[orders['Product'].isin(result)])

import sqlite3 as sql
conn = sql.connect('population.db')
