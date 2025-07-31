# python -m venv myenv
# pip install numpy


from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Using geometry package
radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))

# Using file_operations package
file_path = "homeworks/example.txt"
write_file(file_path, "Hello, this is a test!")
print("File Content:", read_file(file_path))
