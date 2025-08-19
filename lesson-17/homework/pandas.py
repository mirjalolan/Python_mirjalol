import pandas as pd

# Homework1

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)


# Print the first 3 rows of the DataFrame
print(df.head(3))

# Find the mean age of the individuals
mean_age = df['age'].mean()
print(mean_age)

# Select and print only the 'Name' and 'City' columns
print(df[['first_name', 'city']])

# Add a new column 'Salary' with random salary values
df['salary'] = ['466', '469', '798', '4569']
print(df.columns)
print(df.values)

# Display summary statistics of the DataFrame
print(df.describe(include='all'))

# Homework2

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'sales': [5000, 6000, 7500, 8000],
    'expenses': [3000, 3500, 4000, 4500]
}
df = pd.DataFrame(data)
print(df)

# Calculate and display the maximum sales and expenses.
print(df['sales'].max())
print(df['expenses'].max())

# Calculate and display the minimum sales and expenses.
print(df['sales'].min())
print(df['expenses'].min())

# Calculate and display the average sales and expenses.
print(df['sales'].mean())
print(df['expenses'].mean())


# Homework3

data = {
    'category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January' : [1200, 200, 300, 150],
    'February' : [1300, 220, 320, 160],
    'March' : [1400, 240, 330, 170],
    'April' : [1500, 250, 350, 180]
}
df = pd.DataFrame(data)
df.set_index('category', inplace=True)


# Calculate and display the maximum expense for each category
df['max_expense)'] = df.max(axis=1)
print(df)

# Calculate and display the minimum expense for each category.
df['min_expense)'] = df.min(axis=1)
print(df)

# Calculate and display the average expense for each category.
df['avg_expense)'] = df.mean(axis=1)
print(df)
