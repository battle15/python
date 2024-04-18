# Working with Lists

#Looping Through an Entire List
# for loops


#Printing out each name in a list
# For every magician in the list of magicians, print the magician's name
# "magician" is a temporary variable

lesson_break = "--------------------------"
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)

# Doing More Work Within a Loop
# Print a message to each magician 

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
# Indented lines are considered "Inside the loop". As result each line is excuted once for each value in the list
	print(f"I cant wait to see your next trick, {magician.title()}!\n")

# Doing Something After a for loop
# Lines that are not indented in a for loop are not excuted without repetition

print(f"Thank you, everyone. That was a great magic show!")

# Logical Errors
# Occurs when the syntax is correct, but the code does not produce the desired results due problems in its logic.
# TIP: If you expect to see a certain action repeated once for each iten in a list and it's executed only once, 
# Cont. determine whether you need to simply ndent a line or group of line.

print(lesson_break)

print("Exercise 4.1")

# Pizzas: store three names of pizza in a list. Then use a for loop to print the name of each pizza
pizzas = ['cheese','veggie','meat lovers']

for pizza in pizzas:
	print(pizza)
# print a sentence using the name of each pizza. 
	print(f"I really like {pizza}!")
# Add a line outside of the loop, about how much you like pizza. 
print(f"I really wish that I had some pizza")

print(lesson_break)

# Making Numerical Lists
# Using the range() Function
for value in range (1,5):
	print(value)
# This will only print 1 through 4. It only print the first value and stops at the second value
# An argument can be passed to the range() function, and the count will start at 0. Ex range(6) >>> 0 - 5

# Using range() to Make a List of Numbers 
# wrap list() around a range() call to make a list of the numbers

numbers = list(range(1,6))
print(numbers)

# Range can also be used to skip numbers within a range by adding a third argument
# Print all even numbers between 2 and 11
even_numbers = list(range(2,11,2))
print(even_numbers)

# Make a list of the first 10 sqaured numbers
#Create an empty list to add the squared numers to add they populate
squares = []

#for each number(value) in the range of 1 through 11
for value in range(1, 11):
	# Define square as the squared value of each number in the range
	square = value ** 2
	# Add the new value (square) to the empty list (squares) as it populates
	squares.append(square)
# print the newly created list of squared numbers
print(squares)

# A MORE CONSISE WAY

squares = []

for value in range (1,11):
	squares.append(value ** 2)
print(squares)

# Focus on making the code do what you want it to do, then try to make it more effient

#Simple Statistics with a List of Numbers
# minimun, maximum, sum of list of numbers:

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
# List comprehensions allow you to generate a list using one line of code
# combines the for loop and the creation of new elements into one line, and automatically appends each new element
# define the expression before the for the values in the list of the loop
# No colon is used


squares = [value**2 for value in range(1,11)]
print(squares)

# Try to become more comfortable writing comprehensino lists

print(lesson_break)
print("Exercise 4.3")

# Counting to Twenty: use a for loop to print the numbers from 1 - 20, inclusive

for value in range (1,20):
	print(value)

print(lesson_break)
print("Exercise 4.4")

#One Million: Make a list of numbers from one to one million, then create a for loop to print the numbers (STOP it with CTRL-C/Z)
# There is not enough memory to handle one million, therefore 100 will be used instead

one_million = []
for value in range (1, 100):

	one_million.append(value)

print(one_million)

print(lesson_break)
print("Exercise 4.5")

#Summing a Million: Make a list of the numbers from one to one_million (100)
#Cont. Then use min(), and max to to make sure that the list actually starts at 1 and ends at 100
#Cont. Then use sum() to add the numbers

print(min(one_million))
print(max(one_million))
print(sum(one_million))

print(lesson_break)
print("Exercise 4.6")

# Odd Numbers: Use the third argument of the range() function to make a list of odd numbers 1 and 20. 
# Cont. Use a for loop to print each number.

odd_values = []
for value in range (1, 20, 2):
	print(odd_values.append(value))

print(odd_values)


print(lesson_break)
print("Exercise 4.7")

#Threes: Make a list of the multiples of 3 from 3 to 30. Use a loop to print the numbers in the list

threes = []

for value in range(3,30):
	threes.append(value * 3)
print(threes)


print(lesson_break)
print("Exercise 4.8")

#Cubes: Make a list of the first 10 cubes (1 - 10), use a for loop to print out the value of each cube. 

cubes = []
for value in range(1,10):
	cubes.append(value**3)
print(cubes)

print(lesson_break)
print("Exercise 4.9")

# Cube Comprehension: use a list comprehesion to generate a list of the first 10 cubes. 

cubes = [value**3 for value in range(1,10)]
print(cubes)

print(lesson_break)

#Working with Part of a List

# Slicing a List 
# To make a slice, specify the index of the first and last elements you want to work with in the list brackets
# printing indices 0 through 3 

players = ['charles','martina','michael','florence','eli']
print(players[1:4])

#omit the first index in a slice and Python automatically start the slice at the begining

players = ['charles','martina','michael','florence','eli']
print(players[:4])

# Similarly, omit the last index in a slice and Python automatically 
# Cont. starts the slice at the indicated index and contiues to the end of the list

players = ['charles','martina','michael','florence','eli']
print(players[2:])

# slice the Last three players in the list. This will continue to run through the names in the list as the list increases in size

players = ['charles','martina','michael','florence','eli']
print(players[-3:])

#NOTE: a third value in the bracket indicating a slice can be used to skip between items in the specified range.

# Looping Through a Slice

players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# Copying a List
# To copy a list make a splice that omits the first and second index [:]
# [:] Tells Python to start with the first item and end with the last item

my_foods = ['pizza','falafel','carrot cake']

# "friends_food" will produce a copy of "my_foods" by adding [:] to the "my_foods" list
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friend's foods favorite foods are:")
print(friends_foods)

# Adding different items to the original and copied list

my_foods.append('canoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend's foods favorite foods are:")
print(friends_foods)

# Instead of setting the variable "friends_foods" equal to "my_foods" it is better (In this case) to make a copy of it
# Cont. If the second list was set equal to the first list Python would associate the new variable list with the orginal list.
# Cont. Therefore, any modifications made to the additional list, will show for the new variable list.

#======================================
print(lesson_break)
print("Exercise 4.10")

# Slices: Using one of the programs you wrote int this chapter, add several lines to the end of the program that do the following:
# Print the message, "The first three items in the list are:". Then use a slice to print  the first three items of the list

pizzas = ['cheese','veggie','meat lovers']

for pizza in pizzas:
	print(pizza) 
pizzas.append("thin crust")
pizzas.append("stuffed crust")

print(pizzas)

print("The first three items in the list are:")
print(pizzas[:3])

# Print the message, "The first three items from the middle of the list are:". Then use a slice to print three items from the middle of the list

print("The Three items in the middle of the list are:")
print(pizzas[1:4])

# Print the message, "The last three items in the list are are:". Then use a slice to print  the last three items of the list

print("The last three items in the last are:")
print(pizzas[-3:])

#====================================

print(lesson_break)
print("Exercise 4.11")

# My Pizzas, Your Pizzas: Start woth program 4-1 make a copy of "pizzas" and call it "friends_pizzas"

pizzas = ['cheese','veggie','meat lovers']

friends_pizzas = pizzas[:]
# Then:
# Add a new pizza to the original list
pizzas.append("stuffed crust")

# Add a diffent pizza to the list friends_pizza
friends_pizzas.append("thin crust")

# Print seperate list with the messages "My favorite pizzas are:" and "My friend's favorite pizzas are:"

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friends_pizzas)

#=====================================
print(lesson_break)
print("Exercise 4.12")

# More Loops: Choose one of the programs from the lessons in this chapter 

my_foods = ['pizza','falafel','carrot cake']

friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friend's foods favorite foods are:")
print(friends_foods)

my_foods.append('canoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

# Cont. Write two for loops to print each list of foods

print("My foods")
for food in my_foods[:]:
	print(food)

print("\nFriend's foods")
for food in friends_foods[:]:

	print(food)

#=====================================
print(lesson_break)

# Tuples
# Tuples are immutable (values that cannot change) list

# Defining a Tuple 
# Tuples uses parentheses instead of square brackets
# Individual elements can be accessed by using each item's index similar to lists

# Keeping a rectangle's size

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Try to change the dimensions

# dimensions[0] = 250
#Error:  'tuple' object does not support item assignment

# Tuples are technically defined by the presence of a comma. However, paretheses make them look neater and more readable
# To define a tuple with one element, include a trailing comma:
# my_t = (3,)

# Looping Through All Values in a Tuple

dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

# Writing over a Tuple
# A new variable can be assigned to a varible that represents a tuple

dimensions = (200, 500)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

# When compared with list, tuples are simple data structures
# Tuples would be used to store a set of values that should not 
# Cont. be changed thoughout the life of a program

#================================================
print(lesson_break)
print("Exercise 4.13")

#Buffet: Store five buffet items in a tuple

buffet = ('friend chicken', 'corn','mashed potatoes','bread','green beans')

#Use a for loop to print each food that the restaurant offers

for food in buffet:
	print(food)

#Try to modify one of the items and make sure that Python rejects the change

# buffet[1] = 'coleslaw'

# Error: 'tuple' object does not support item assignment

# Replace two items with different foods. 
# 	corn -> coleslaw and green beans -> peas 
# Cont. Add a line that rewrite the tuple
buffet = ('fried chicken', 'coleslaw','mashed potatoes','bread','peas')

# Then use a for loop to print each of the items on the revised menu

print("\n")
for food in buffet:
	print(food)

#================================================
print(lesson_break)

# Styling Your Code

# The Style Guide
# Python Enanchement Proposal (PEP)
# Programmers are encouraged to write code that's easier to read

# Indentation
# Use 4 spaces per indentation level
# Make sure that the code editor TAB key is set to for spaces
# In a word processing document use 4 spaces

# Line Length
# Each line should be less than 80 characters
# Keep all comments to 72 characters per line
# Most editors allow you to set up a visual cue, usually a verticle line on your screen
# Cont. that shows you where the limits are

#Blank Lines

# To group parts of your program by using blank line. 
# Use one blank line inbetween groups of code
# Blank line affect the readability of the code

# PEP link: https://python.org/dev/peps/pep-0008/



