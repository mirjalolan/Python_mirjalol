# 1
# Write a Python script to sort (ascending and descending) a dictionary by value.
strings = {'Abror': '460', 'Mirjajon': '489', 'Asror': '486'}
sorted_asc = sorted(strings.items(), key=lambda item: item[1])
print(sorted_asc)
sorted_desc = sorted(strings.items(), reverse=True)
print(sorted_desc)

# 2
# Write a Python script to add a key to a dictionary.
strings = {'Abror': '460', 'Mirjajon': '489', 'Asror': '486'}
strings.update([('Shaxzod', '500')])
print(strings)

strings['Ozod'] = '550'
print(strings)

# 3
# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# 4
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input("Please enter the number: "))
new_dic = {x: x*x
           for x in range(1, n+1)
           }
print(new_dic)

# 5
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are the square of the keys.
n = 15
new_dic = {x: x*x
           for x in range(1, n+1)
           }
print(new_dic)

# sets
# 1
# Write a Python program to create a set.
my_set = {11, 11, 516, 168, 8946}
print(my_set)

# 2
# Write a Python program to iterate over sets.
my_set = {11, 11, 516, 168, 8946}
for i in my_set:
    print(i)

# 3
# Write a Python program to add member(s) to a set.
my_set = {11, 11, 516, 168, 8946}
my_set.add(15)
print(my_set)

# 4
# Write a Python program to remove item(s) from a given set.
my_set = {11, 11, 516, 168, 8946}
my_set.remove(11)
print(my_set)

# 5
# Write a Python program to remove an item from a set if it is present in the set.
my_set = {11, 11, 516, 168, 8946}
my_set.discard(15)
print(my_set)
