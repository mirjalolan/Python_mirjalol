# Find all questions that were created before 2014
import pandas as pd
import datetime as dt
df = pd.read_csv('tackoverflow_qa.csv')
dd = pd.read_csv('titanic.csv')

df['creationdate'] = pd.to_datetime(df['creationdate'])
print(df[df['creationdate'].dt.year < 2014])

# Find all questions with a score more than 50
print(df[df['score']>50])

# Find all questions with a score between 50 and 100
print(df[df['score'].between(50,100)])

# Find all questions answered by Scott Boston
print(df[df['ans_name']=='Scott Boston'])

# Find all questions that were created between March, 2014 and October 2014 
# that were answered by Unutbu and 
# have score less than 5.
df['creationdate'] = pd.to_datetime(df['creationdate'])
creation_year = (df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31')
answerer = df['ans_name'] == 'Unutbu'
score = df['score'] < 5
mask = creation_year & answerer & score  
result = df[mask]
print(result)

# Find all questions that have score between 5 and 10 or 
# have a view count of greater than 10,000
score = df['score'].between(5,10)
view_count = df['viewcount']>10000
print(df['score'] | df['viewcount'])

# Find all questions that are not answered by Scott Boston
answerer = df['ans_name'] != 'Scott Boston'
print(df[answerer])

# Select Female Passengers in Class 1 with Ages between 20 and 30: 
# Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
class_check = dd['Pclass'] == 1
age_check = dd['Age'].between(20,30)
gender_check = dd['Sex'] == 'female'

result = dd[class_check & age_check & gender_check]
print(result)

# Filter Passengers Who Paid More than $100: 
# Create a DataFrame with passengers who paid a fare greater than $100.
print(dd[dd['Fare'] > 100])

# Select Passengers Who Survived and Were Alone: 
# Filter passengers who survived and were traveling alone 
# (no siblings, spouses, parents, or children).
parent_check = dd['Parch'] == 0
sibling_check = dd['SibSp'] == 0
survival_check = dd['Survived'] == 0

result = dd[parent_check & sibling_check & survival_check]

print(result)

# Filter Passengers Embarked from 'C' and Paid More Than $50: 
# Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
embark_check = dd['Embarked'] == 'C'
fare_check = dd['Fare'] > 50

result = dd[embark_check & fare_check]
print(result)


# Select Passengers with Siblings or Spouses and Parents or Children: 
# Extract passengers who had both siblings or spouses aboard and parents or children aboard.
sibling_check = dd['SibSp'] != 0
parent_check = dd['Parch'] != 0
result = dd[sibling_check & parent_check]
print(result)

# Filter Passengers Aged 15 or Younger Who Didn't Survive: 
# Create a DataFrame with passengers aged 15 or younger who did not survive.
age_check = dd['Age'] <= 15
print(dd[age_check])


# Select Passengers with Cabins and Fare Greater Than $200: 
# Extract passengers with known cabin numbers and a fare greater than $200.
cabin_check = dd['Cabin'].notna()
fare_check = dd['Fare'] > 200
result = dd[cabin_check & fare_check]
print(result)


# Filter Passengers with Odd-Numbered Passenger IDs: 
# Create a DataFrame with passengers whose PassengerId is an odd number
odd_id = dd[dd['PassengerId'] % 2 != 0]
print(odd_id)

# Select Passengers with Unique Ticket Numbers: 
# Extract a DataFrame with passengers having unique ticket numbers.
unique_check = dd['Ticket'].duplicated(keep=False)
print(dd[unique_check])

# Filter Passengers with 'Miss' in Their Name and Were in Class 1: 
# Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
import string as str
class_check = dd['Pclass'] == 1
gender_check = dd['Sex'] == 'female'
name_check = dd['Name'].str.contains('Miss')
result = dd[class_check & gender_check & name_check]
print(result)
