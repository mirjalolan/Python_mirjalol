# 1
# Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

birth_year = int(input("Please enter your birth year: "))
name = input("Please enter your name: ")
age = 2025 - birth_year
print(f"Hello, {name}. Your age is {age}. ")

# 2
# Extract Car Names
# Extract car names from the following text:

def find_car(text, car_names):
    result = []
    for i in car_names:
        if i.lower() in text.lower():
            result.append(i)
    return result


txt = 'LMaasleitbtui'
car_names = ["BMW", "Mercedes", "Mazda", "Toyota", "Ford"]
print(find_car(txt, car_names))


# 3
# Extract Car Names
# Extract car names from the following text:

def car_find(text, car_names):
    result = []
    for i in car_names:
        if i.lower() in text.lower():
            result.append(i)
    return result


txt = 'MsaatmiazD'
car_names = ["BMW", "Mercedes", "Mazda", "Toyota", "Ford"]
print(car_find(txt, car_names))


# 4
# Extract Residence Area
# Extract the residence area from the following text:

def find_residence(text):
    word = text.split()
    if "from" in word:
        index = word.index("from")
        if index + 1 < len(word):
            return word[index+1]
    else:
        return None


txt = "I'am John. I am from London"
print(find_residence(txt))


# 5
# Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

word = input("Please enter the word: ")
re_word = word[::-1]
print(re_word)

# 6
# Count Vowels
# Write a Python program that counts the number of vowels in a given string.

vowels = "aouei"
text = input("Please enter the word: ")
new_text = 0
for i in text:
    if i.lower() in vowels:
        new_text += 1
print(new_text)

# 7
# Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = input("Please enter the list of numbers: ")
new_num = list((map(int, numbers.split(","))))
max_value = max(new_num)
print(f"Your max is {max_value}")

# 8
# Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Please enter the word: ")
if word == word[::-1]:
    print("Your word is polindrome! ")
else:
    print("Your word is NOT polindrome! ")

# 9
# Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Please enter your email: ")
if "@" in email:
    new_email = email.split("@")[1]
    print(new_email)
else:
    print("Invalid email")

# 10
# Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string
password_length = 12
letters = string.ascii_letters   
digits = string.digits           
special_chars = "!@#$%^&*()-_=+[]{}<>?/|"
all_chars = letters + digits + special_chars
password = ''.join(random.choice(all_chars) for _ in range(password_length))
print("Generated Password:", password)
