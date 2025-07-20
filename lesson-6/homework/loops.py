# 1
txt = "abcabcabcdeabcdefabcdefg"
vowels = ['a', 'e', 'i', 'o', 'u']
index = 2
while index < len(txt) - 1:
    if txt[index] not in vowels:
        txt = txt[:index + 1] + '_' + txt[index + 1:]
        vowels.append(txt[index])
        index += 4
    else:
        index += 1
print(txt)


# 2
# The provided code stub reads an integer, n, from STDIN.
# For all non-negative integers i where 0 <= i < n, print i^2.

number = int(input("Please enter the number: "))

for i  in range(number):
    print(i**2)

# 3
# Print first 10 natural numbers using a while loop
result = 1
while result<11:
    print(result)
    result += 1

# 4
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 5
total = 0
number = int(input("Please enter the number: "))
for i in range(1, number+1):
    total += i
print(total)

# 6
number = int(input("Please enter the number: "))
result = []
for i in range(1, number+1):
    if i % 2 == 0:
        result.append(i)
print(result)

# 7
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    print(i)

# 8
number = int(input("Pleasen enter the number: "))
list_number = list(str(number))
for i in list_number:
    a = len(list_number)
print(a)

# 9
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# 10
list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
    print(i)

# 11
for i in range (-10, 0):
    print(i)

# 12
for i in range(0,5):
    print(i)
print("Done")

# 13
factorial = 1
number = int(input("Please enter the number: "))
for i in range(1, number + 1):
    factorial *= i
print(factorial)
