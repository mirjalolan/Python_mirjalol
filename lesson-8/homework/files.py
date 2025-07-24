# 1
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cant be divided by zero")

# 2
# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    a = int(input("Please enter the number: "))
    print(a)
except ValueError:
    print("Only take integers")

# 3
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open('my_files\my_new_file.txt') as o:
        for i in o:
            print(i)
except FileNotFoundError:
    print("File not found")

# 4
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    age = int(input("Please enter your age: "))
    print(len(age))
except TypeError:
    print("Age itself cant be used in function ")

# 5
# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open("D:\\Python files\\Python_learning\\homeworks\\example.txt", 'r')as p:
        for i in p:
            print(i.strip())
except PermissionError:
    print("You have no acces to that file")

# 6
# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    fruits = ['apple', 'banana', 'pear']
    print(fruits[4])
except IndexError:
    print("Index is out of range")

# 7
# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    number = input("Please enter a number: ")
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nInput cancelled by the user.")

# 8
# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cant be divided by zero")

# 9
# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open("homeworks\example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Encoding issue: Unable to decode the file using UTF-8.")

# 10
# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    numbers = [1, 2, 3, 4]
    a = numbers.push(6)
    print(a)
except AttributeError:
    print("No such attribute found")


# Write a Python program to read an entire text file.
with open('homeworks\\example.txt')as text:
    content = text.read()
    print(content)

# Write a Python program to read first n lines of a file.
n = int(input("Please enter the number of lines you want to read: "))
with open('homeworks\\example.txt')as text:
    for i in range(n+1):
        line = text.readlines()
        print(line)

# Write a Python program to append text to a file and display the text.
with open('homeworks\\example.txt', 'a')as text:
    text.write('eunvpiae')
with open('homeworks\\example.txt', 'r')as text:
    for i in text:
        print(i.strip())

# Write a Python program to read a file line by line and store it into a list.
with open('homeworks\\example.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
print(lines)

# Write a Python program to find the longest words.
with open('homeworks\\example.txt', 'r') as file:
    words = file.read().split()
max_length = max(len(word) for word in words)
max_word = [word for word in words if len(word) == max_length]
print(max_word)

# Write a Python program to count the number of lines in a text file.
with open('homeworks\\example.txt', 'r') as file:
    lines = file.readlines()
print("Number of lines:", len(lines))

# Write a Python program to write a list to a file.
students = ['Ali', 'Akbar', 'Abror']

try:
    with open('homeworks\\practise.txt', 'w') as file:
        for student in students:
            file.write(student + '\n')
except FileExistsError:
    print("File already exists")

with open('homeworks\\practise.txt', 'r') as file, open('homeworks\\practise.txt', 'r')as name:
    for line1, line2 in zip(file, name):
        combined = line1.strip() + ' ' + line2.strip()
        print(combined)



import random
with open('homeworks\\example.txt', 'r') as file:
    lines = file.readlines()
random_line = random.choice(lines)
print(random_line.strip())


with open('homeworks\\example.txt', 'r') as file:
    content = file.read().replace('\n', '')
print(content)

with open('homeworks\\example.txt', 'r') as file:
    text = file.read()
    words = text.split()
    print(len(words))

import os
with open('homeworks\\example.txt', 'r') as file:
    text = file.read()
    char_list = []
    char_list.extend(list(text))
print(char_list)

