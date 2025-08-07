# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import date

year_born = int(input('Please enter your year: '))
month_born = int(input('Please enter your month: '))
day_born = int(input('Please enter your day: '))

today = date.today()
birthday = date(year_born, month_born, day_born)

dif = (today - birthday).days

year = dif//365
months = (dif % 365)//30
days = (dif % 365) % 30

print(f'You lived {year} years, {months} months, {days} days')


# Days Until Next Birthday: Similar to the first exercise, but this time,
# calculate and print the number of days remaining until the user's next birthday.

from datetime import date

year_born = 2026
month_born = int(input('Please enter your month: '))
day_born = int(input('Please enter your day: '))

today = date.today()
birthday = date(year_born, month_born, day_born)

dif = (birthday-today).days

print(dif)

# Meeting Scheduler: Ask the user to enter the current date and time,
# as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

# Ask the user to enter the current date and time in 'YYYY-MM-DD HH:MM' format
current_date = input('Please enter the current date: ')

# Convert the input string to a datetime object
start_date = datetime.strptime(current_date, '%Y-%m-%d %H:%M')

# Ask the user to enter meeting duration in hours
meeting_hour = int(input('Please enter the meeting duration in hours: '))

# Ask the user to enter meeting duration in minutes
meeting_minutes = int(input('Please enter the meeting duration in minutes: '))

# Create a timedelta object using the entered hours and minutes
meeting_duration = timedelta(hours=meeting_hour, minutes=meeting_minutes)

# Add the timedelta to the start time to get the meeting end time
end_date = start_date + meeting_duration

# Format and print the meeting end time
print(end_date)

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone,
# and then convert and print the date and time in another timezone of their choice.

# Import datetime and zoneinfo modules
from datetime import datetime
from zoneinfo import ZoneInfo


# Ask the user to enter a date and time in 'YYYY-MM-DD HH:MM' format
current_date = input('Please enter the current date: ')
# Convert the input string into a datetime object
dt = datetime.strptime(current_date, '%Y-%m-%d %H:%M')

# Ask the user for their current timezone (e.g., 'Asia/Tashkent')
current_timezone = input('Enter your timezone: ')

# Set the timezone of the entered datetime using zoneinfo
dt = dt.replace(tzinfo=ZoneInfo(current_timezone))

# Ask the user for the target timezone (e.g., 'America/New_York')
target_timezone = input('Enter the timezone: ')

# Convert the datetime to the target timezone
converted_time = dt.astimezone(ZoneInfo(target_timezone))

# Print the converted date and time in the target timezone
print(converted_time)


# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and
# then continuously print the time remaining until that point in regular intervals (e.g., every second).
from datetime import datetime
import time

# Ask the user to enter a future date and time
target_input = input("Enter the future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

print("\nCountdown started...\n")

# Loop until current time reaches target time
while True:
    now = datetime.now()
    time_left = target_time - now

    if time_left.total_seconds() <= 0:
        print("⏰ Time's up!")
        break

    # Clear previous line and print updated time left
    print("Time left:", time_left, end='\r')
    time.sleep(1)  # Wait 1 second before updating


#6

#Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.

import re

email = input('Please enter the email address: ')

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print('Email is valid')
else:
    print('Invalid email')

#7

# Phone Number Formatter: Create a program that takes a phone 
# number as input and 
# formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".


phone_number = int(input('Please enter your number: '))

digits = str(phone_number)

if len(digits) == 12:
    formatted = f'{digits[:3]}-{digits[3:5]}-{digits[5:]}'
    print(formatted)
else:
    print('Invalid phone number: ')    

#8

#Password Strength Checker: Implement a password strength checker. 
# Ask the user to input a password and check if it meets certain 
# criteria (e.g., minimum length, contains at least one uppercase 
# letter, one lowercase letter, and one digit).


# Step 1: Ask the user to enter a password
password = input('Enter the password: ')

# Step 2: Initialize flags for lowercase, uppercase, and digit
lowercase = False
uppercase = False
digit = False

# Step 3: Check if the password length is at least 8 characters
length = len(password)>= 8

# Step 4: Loop through each character in the password
#         - Check if it's a lowercase letter → set lowercase flag True
#         - Check if it's an uppercase letter → set uppercase flag True
#         - Check if it's a digit → set digit flag True
for i in password:
    if i.islower():
        lower = True
    elif i.isupper():
        upper = True
    elif i.isdigit():
        digit = True

# Step 5: After the loop, check if all conditions are met:
#         - Length ≥ 8
#         - At least one lowercase
#         - At least one uppercase
#         - At least one digit

if lower and uppercase and digit and length:
    print('Passwod is strong')
else:
    print('Password is weak')

#9 

# Word Finder: Develop a program that finds all occurrences of a 
# specific word in a given text. Ask the user to input a word, and 
# then search for and print all occurrences of that word in a 
# sample text
import re

text = 'I want to sleep well and feed enough. I want to be data analyst!'

word = input('Enter the word you want to find: ')
words_found = re.findall(word, text)
print(words_found)

# 10

# Date Extractor: Write a program that extracts dates from a given text. 
# Ask the user to input a text, and then identify and print all the 
# dates present in the text.
import re

text = input('Enter the text: ')

pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{4}|\d{4}-\d{1,2}-\d{1,2})\b'

found = re.findall(pattern, text)

if found:
    print(found)
else:
    print('No matches found')
