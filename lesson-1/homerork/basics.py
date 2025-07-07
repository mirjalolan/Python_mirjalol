# # Given diameter of circle. Find its length.
a = float(input("Enter the diameter in cm: "))
length = round((3.14 * a), 2)
print(f"The length of circle is {length}")  


# # Given two numbers a and b. Find their mean.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
mean = round(((a+b)/2),2)
print(f"Mean is {mean}")


# Given two numbers a and b. Find their sum, product and square of each number.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
sum = a+b
product = a*b
square_a = round((a**0.5),2)
square_b = round((b**0.5),2)
print(f"Sum: {sum}, product: {product}, square of a: {square_a}, sqaure of b: {square_b}")

# # Given a side of square. Find its perimeter and area.
a = int(input("Enter the length in cm: "))
result = 4 * a
print(f"Perimeter of square is {result}")
