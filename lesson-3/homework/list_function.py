#1
#Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'banana', 'pineapple', 'pear', 'peach']
print(fruits[2])

#2
#Create two lists of numbers and concatenate them into a single list.
numbers_1 = [1,2,3]
numbers_2 = [4,5,6]
numbers_1.extend(numbers_2)
print(numbers_1)

#3
#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1,2,3,4,5,6,7]
first_num = numbers[0]
middle_num = numbers[len(numbers)// 2]
last_num = numbers[-1]
new_list = [first_num, middle_num, last_num]
print(new_list)

#4
#Create a list of your five favorite movies and convert it into a tuple.
movies = ['Intersteller', 'Joker', 'LOTR', 'GOT', 'Breaking Bad']
films = tuple(movies)
print(films)

#5
#Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['London', 'Barcelona', 'Florence', 'Edinburgh']
cities.index("Paris")

#6
#Create a list of numbers and duplicate it without using loops.
numbers = [1,2,3,4]
figures = [1,2,3,4]
numbers.extend(figures)
print(numbers)

#7
#Given a list of numbers, swap the first and last elements.
numbers = [1,2,3,4]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

#8
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[2:7])

#9
#Create a list of colors and count how many times "blue" appears in the list.
colors = ['blue', 'blue', 'red', 'purple', 'green']
print(colors.count('blue'))

#10
#Given a tuple of animals, find the index of "lion".
animals = ('lion', 'leopard', 'cheetah', 'gepard','jaguar')
print(animals.index('lion'))

#11
#Create two tuples of numbers and merge them into a single tuple.
colors = ('blue', 'blue', 'red', 'purple', 'green')
animals = ('lion', 'leopard', 'cheetah', 'gepard','jaguar')
colors += animals
print(colors)

#12
# Given a list and a tuple, find and print their lengths.
animals = ('lion', 'leopard', 'cheetah', 'gepard','jaguar')
colors = ['blue', 'blue', 'red', 'purple', 'green']
print(len(animals))
print(len(colors))

#13
#Create a tuple of five numbers and convert it into a list.
colors = ['blue', 'blue', 'red', 'purple', 'green']
new_colors = list(colors)
print(new_colors)

#14
#Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (1,2,3,4,5,6)
print(max(numbers))
print(min(numbers))

#15
#Create a tuple of words and print it in reverse order.
animals = ('lion', 'leopard', 'cheetah', 'gepard','jaguar')
new_animals = animals[::-1]
print(new_animals)
