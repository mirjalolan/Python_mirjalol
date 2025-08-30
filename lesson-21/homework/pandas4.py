import matplotlib.pyplot as plt
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis='columns')
print(df1[['Student_ID', 'Average']])

# Exercise 2: Find the student with the highest average grade.
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis='columns')
print(df1[df1['Average'] == df1['Average'].max()])

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis='columns')
print(df1[['Student_ID', 'Total']])


data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
df_long = df2.melt(id_vars='Date', var_name='Product', value_name='Sales')
result = df_long.groupby('Product')['Sales'].sum()
print(result)

# Exercise 2: Find the date with the highest total sales.
df_long = df2.melt(id_vars='Date', var_name='Product', value_name='Sales')
result = df_long.groupby('Date')['Sales'].sum()
max_sales = result.max()
print(max_sales)
max_date = result.idxmax()
print(max_date)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df_long = df2.melt(id_vars='Date', var_name='Product', value_name='Sales')
df_long['Pct_change'] = df_long.groupby('Product')['Sales'].pct_change()*100
print(df_long.head())

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

df2.set_index("Date")[["Product_A", "Product_B", "Product_C"]].plot(marker="o")

plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend(title="Product")
plt.show()



data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

avg_salary = df3.groupby("Department")["Salary"].mean()
print(avg_salary)

most_exp = df3.loc[df3["Experience (Years)"].idxmax()]
print(most_exp)

min_salary = df3["Salary"].min()
df3["Salary Increase"] = ((df3["Salary"] - min_salary) / min_salary) * 100
print(df3)

import matplotlib.pyplot as plt

df3["Department"].value_counts().plot(kind="bar")

plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
