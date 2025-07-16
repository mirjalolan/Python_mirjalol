#1
def is_leap (year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2030))

#2
number = int(input("Please enter the number: "))
if 1<= number <= 100: 
    if number % 2 == 0 and 6<=number<=20:
        print("Weird")
    elif number % 2 == 0 and 2<=number<=5:
        print("Not weird")
    elif number % 2 != 0:
        print("Weird")
    elif number % 2 == 0 and number > 20:
        print("Not weird")
else:
    print("Your number is out of range! ")

#3
a = int(input("Please enter the number (a): "))
b = int(input("Please enter the number (b): "))
if a % 2 == 0 and b % 2 == 0:
    print("Both are even! ")
elif b % 2 == 0 and a % 2 != 0 :
    print("B is even! ")
elif a % 2 == 0 and b % 2 != 0:
    print("A is even! ")
else:
    print("None of them are even! ")
