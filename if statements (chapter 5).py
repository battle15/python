# If Statements
# A Simple Example

lesson_break = "=============================="
# Printing car names in either .title() or .upper
cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# If and else statements both end with colons

# Conditional Tests 
# Contains a statement that can be evaluated as either True or False. 
# If True, the statement is executed
# If False, the statement is ignored

# Checking for Equality

car = 'bmw'
car == 'bmw'
# True 

# Equality operators (==) returns True if the value is a match, 
# Cont. And False if the value does not match

car = 'audi'
car == 'bmw'

# False

#Ignoring Care When Checking for Equality 

car = 'Audi'
car == 'audi'

# False

# Converting the variable before doing a comparison

car = 'Audi'
car.lower() == 'audi'

# True
# This will not affect the original variable. 
# This is best for when case is not as important for comparisons
print(car)

#======================================

# Checking for Inequality
# Combine an exclamation point and an equal sign (!=), not equal to

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")


# Numberical Comparisons

age = 18
age == 18

# True

# Test if two numbers are not equal

answer = 17

if answer != 42:
	print("That's not the correct answer, please try again!")

age = 19
# Less than
age < 21
# True

# Less than or equal to 
age <= 21
# True

# Greater than 
age > 21
# False

# Greater than or equal to

age >= 21
# False

#==================================

#Checking Mulitple Conditions
# Keywords: AND or OR

# Using and to Check Multiple Conditions

# AND

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21

# False
# Because one test failed (age_1 >= 21), the program returns False

age_0 = 22
age_1 = 23
age_0 >= 21 and age_1 >= 21

#True

# To inprove readability at parentheses around individual tests

(age_0 >= 21) and (age_1 >= 21)

#Using OR to Check Multiple Conditions

# OR passes when either or both of the individual test pass. 

age_0 = 33
age_1 = 18
(age_0 >= 32) or (age_1 >= 21)
# True

# OR only fails when both test failes 

age_0 = 18

(age_0 >=21) or (age_1 >= 21)
# False

# Checking Whether a Value Is in a List
# Using the keyword IN

# Check for toppings

requested_toppings = ['mushrooms','onions','pineapple']
true_false = 'mushrooms' in requested_toppings
print(true_false)
# True

true_false = 'pepperoni' in requested_toppings
print(true_false)
# False

# Checking Where a Value Is Not in a List
# Using the keyword NOT

# Checking if user has been banned

banned_users =['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish")

# Python returns True a the line was executed

# Boolean Expressions
# A Boolean value is either True or False
# Often used to keep track of certain conditions

game_active = True
can_edit = False

print(lesson_break)
print("Exercise 5-1")

# Conditional Test: Write a series of conditional test. 
# Cont. Print a statement descibing each test and prediction of the result

food = 'meat'
print("Is food == 'meat'? I predict True")

print(food == 'meat')

print("\nIs food == 'shoe'? I predict False")
print(food == 'shoe')

print(lesson_break)
print("Exercise 5-2")


# More Conditional Tests

# Have at least on True and one False result each of the following:
# Test for equality and inequality in strings
colors = 'red'

print(colors == 'red')
# Should be True

print (colors == 'yellow')
# Should be false

# Test using the lower() method 

colors = 'Red'
print( colors.lower() == 'red')
# Should be True



# Numerical test inviling equality and inequality
# Cont. Greater than and less than, greater than or equal to, and less than or equal to

weight_0 = 110

# Greater than
# True
print((weight_0 > 101))

#False
print((weight_0 > 123))

# Greater than or equal to

#True
print((weight_0 >= 101))

#False
print((weight_0 >= 123))

# Less than
# True
print((weight_0 < 123))

# False
print((weight_0 < 101))

# Less than or equal to
#True 
print((weight_0 <= 123))

#False
print((weight_0 <= 101))

print("=====")

# Tests using the AND keyword and the OR keyword

weight_0 = 110
weight_1 = 130

# AND
# True
print((weight_0 < 123 and weight_1 > 120))

# False
print((weight_0 > 123 and weight_1 > 120))
# OR
# True
print((weight_0 < 123 or weight_1 < 120))

# False
print((weight_0 > 123 or weight_1 < 120))

# Test whether an item is IN a list

colors = ['red','yellow','blue']
#True
print('yellow' in colors)

#False
print('green' in colors)

# Test whether an item is NOT in a list
colors = ['red','yellow','blue']

#True
print('black' not in colors)

#False
print('blue' not in colors)

#====================
print(lesson_break)

# If Statements
# Simple if Statements 
# If the person can vote

age = 19 
if age >= 18:
	print(" You are old enough to vote!")
	# This next line will run in this loop as long as the condtions are meet
	print(" Have you registered to vote yet?")

# if-else Statements
# Similar to an if statement, 
#Cont. but the else statement is excuted if the conditional  test fails

age = 17
#age = 19 
if age >= 18:
	print(" You are old enough to vote!")
	# This next line will run in this loop as long as the condtions are meet
	print(" Have you registered to vote yet?")

else:
	print("Sorry, you are too young to vote.")
	print("Please register as soon are you turn 18")

print("============")

# The if-else statement works when there are only 2 possible situations

# The if-elif-else Chain
# Used to test more than two situations

# Amuesement Park charging different rates for different groups

# Admission for anyone under age 4 is free
# Admission for anyone between the ages of 4 and 18 is $25
# Admission for anyone age 18 or older is $40
age = 12

if age < 4:
	print("Your admission cost is free")
elif age < 18:
	print("Your admission cost is $25")
else:
	print ("Your admission cost is $40")

# A more concise way

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else: 
	price = 40

print(f"Your admission cost is ${price}")

# more efficient and easier to modify

# Using Multiple elif Blocks
# Addition discount for seniors
# 65 or older pays half the regular admission or 20:

age = 32

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
# Going in order, only the ages that makes it to the else block
# Cont. are 65 and older
else: 
	price = 20

print(f" Your admission cost is ${price}")

# Omitting the else Block
# an else block is not required at the end of an if-else chain
# Sometimes omitting the else block provides more clarity

age = 43

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}")

# If there are specific condition that are being tested
# Cont. use a final elif statement omit the else block.
# You'll gain confidence that you code will only
# Cont. run uder the correct conditions

print(lesson_break)
# Testing Multiple Conditions 
# Test if both topping on a two-toppings pizza is true

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

# In this example using if statements work best 
# Cont. because all conditions are checks
# An if-elif-else chain, would only check the first condition
# Cont. And if it is met, then it would ignore the remaining conditions
# if-elif-else statements ONLY pass one block of conditions

print(lesson_break)
print("Exercise 5-3")
#Alien Colors #1 : Create a variable called alient_color and 
#Cont. assign it a value of 'green', 'yellow,' or 'red'

alien_color = 'green'
# Write an if statement to test whether the alien's color is green. 
# If it is, print a message that the player just earned 5 points.

if alien_color == 'green':
	print("5 points scored")

# Write one version of this program that passes the if test 
alien_color = 'green'

if alien_color == 'green':
	print("5 points scored")

# Cont. and another that fails (result: No output)

alien_color = 'red'

if alien_color == 'green':
	print("5 points scored")

# No output 

print(lesson_break)
print("Exercise 5-4")
# Alien Colors #2: Write an if-else statement with the previous color
if alien_color == 'green':
	print("")
else:
	print("")
# If green, print a statement that the player earned 
# Cont. 5 points for shooting the alien
# If not green, print a statement that the player earned 10 points
# Write a version that runs the if block on one that runs the else block
# if block
alien_color = 'green'

if alien_color == 'green':
	print("Green alien: 5 points")
else:
	print("Different color alien: 10 points")

# else block

alien_color = 'red'

if alien_color == 'green':
	print("Green alien: 5 points")
else: 
	print("Different color alien: 10 points")

print(lesson_break)
print("Exercise 5-5")
# Alien Colors #3: Turn the if-else chain into a if-elif-else chain
# Green, print message for earned 5 points
# Yellow, print message for earned 10 points
# Red, print messgae for earned 15 points
# Write three version of the program for each color

if alien_color == 'green':
	print("5 points scored")
elif alien_color == 'yellow':
	print("10 points scored")
else:
	print("15 points scored")

# Green Alien

alien_color = 'green'

if alien_color == 'green':
	print("5 points scored")
elif alien_color == 'yellow':
	print("10 points scored")
else:
	print("15 points scored")

# Yellow Alien
alien_color = 'yellow'

if alien_color == 'green':
	print("5 points scored")
elif alien_color == 'yellow':
	print("10 points scored")
else:
	print("15 points scored")

# Red Alien

alien_color ='red'
	
if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
else:
	points = 15

print(f"{points} points scored")

print(lesson_break)
print("Exercise 5-6")

# Stages of Life: Write an if-elif-else chain the determines
# Cont. a person stage of life.
# Set a value for the variable age and then:
# Less that 2 years old, print baby
# At least 2 but less than 4, print toddler
# At least 4 but less than 13, print kid
# At least 13 but less than 20, print teenager
# At least 20 but less than 65, print adult
# 65 and older, print elder
# message = " You are an {stage_of_life}"

age = 13

if age < 2:
	stage_of_life = 'baby'
elif age < 4: 
	stage_of_life = 'toddler'
elif age < 13:
	stage_of_life = 'kid'
elif age < 20:
	stage_of_life = 'teenager'
elif age < 65:
	stage_of_life = 'adult'
else:
	stage_of_life = 'elder'

print(f"You are a(n) {stage_of_life}")



print(lesson_break)
print("Exercise 5-7")

# Favorite Fruit: Make a list of fav fruits
# Create a series of INDEPENDENT if statements to check for certain fruit
# Make a list with three fav fruits named favorite_fruits

favorite_fruit = ['apples','oranges','kiwi']

# Write 5 if statements, checking if certain fruits are in the list
# If the fruit is in the list print a statment

# 3 true 
if 'apples' in favorite_fruit:
	print("I love apples!")
if 'oranges' in favorite_fruit:
	print("I love oranges!")
if 'kiwi' in favorite_fruit:
	print("I love kiwi!")

# 2 false 

if 'pears' in favorite_fruit:
	print("I love pears!")

if 'bananas' in favorite_fruit:
	print("I love bananas!")
# These statements do not have an output as the items are not in the list.

print(lesson_break)

# Using if Statements in Lists
# Checking for Special Items

# Announcing the added toppings to a pizza as they are being added

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}")

print(f"Finished making your pizza")

# Scenario: Pizzeria runs out of green peppers
# Add an if statement regarding the missing item

requested_toppings = ['mushrooms','green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print(f"Sorry, we are out of {requested_topping}")
	else: 
		print(f"Adding {requested_topping}")
print(f"\nFinished making your pizza!")

print(lesson_break)

# Checking that a List is Not Empty
# Check if list is empty
# If Empty, prompt the user and confirm that they want a plain pizza
# If not empty, build the pizza like previous examples

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("Finished making your pizza")
else:
	print("Are you sure you want a plain pizza?")

print(lesson_break)

# Remember: When the name of a list is in an if statement
# Cont. Python returns True if the list contains at least one item
# Cont. An empty list evaluates to false

# Using Multiple Lists

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we do not have {requested_topping}. ")
print(f"\nFinished making your pizza!")

print(lesson_break)
print("Exercise 5-8")

# Hello Admin: Make a list of five or more usernames, including 'admin'
# Cont.Loop through the list and print a welcome greeting for each user
# If the user name is 'admin', print a special greeting.
# Otherwise, print a generic greeting

users = ['admin','tom1','mary2','cindy1','lucy5']

for user in users:
	if user == 'admin':
		print(f"Hello {user}, Would you like to see a status report?")
	else:
		print(f"Hello {user}, Welcome back!")

print(lesson_break)
print("Exercise 5-9")

# No Users: Add an if test to previous exercise 
# Cont. to make sure that the list is not empty
# If list is empty print, "We need to find some users!"
# Remove all of the usernames from the list
# Cont. make sure that the correct message is printed

users = []

if user in users:
	for user in users:
		if user == 'admin':
			print(f"Hello {user}, Would you like to see a status report?")
		else: 
			print(f"Hello {user}, Welcome back!")
else: 
	print("We need to find some users!")


print(lesson_break)
print("Exercise 5-10")

# Checking Usernames: Simulate how websites ensures unique usernames
# Make a list of five usernames or more names called current_users
current_users = ['tom1','admin','mary2','cindy1','lucy5']

# Make another list of five usernames called new_users
# Make sure one or two of the usernames are in the current_users list
new_users = ['steven4','tom1','aDmIn','BOB','Jack1e']

# Loop through the new_users list to see if each new username has 
# Cont. already been used.
# Cont. If it has, print "Username Taken"
# Cont. Print "Username Available", if the username has not been used

for username in new_users:
	if username.lower() in current_users:
		print(f"Username, {username}, is taken")
	else: 
		print(f"Username, {username}, is Available")


# Make sure the comparison is case insensitive
# Cont. make a copy of current_users containing the lower case versions
# COME BACK TO: Figure out how to copy make current_user list case insensitive


print(lesson_break)
print("Exercise 5-11")

# Ordinal Numbers: Ordinal numbers indicate their position in a list 
# Cont. Such as '1st' or '2nd'
# Most ordinal numbers end with 'th', except 1, 2, and 3

# Store the numbers 1 through 9 in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list
for number in numbers:

	if number == 1:
		print (f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")

# Use an if-elif-else chain inside the loop to print the proper
# Cont. ordinal ending for each number.
# Output: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
# Each input should be on a separate line


# Fizzbuzz
# 1 - 100
# 3 = fizz
# 5 = buzz
# multiples of three and 5 = fizz buzz
print(lesson_break)

numbers = list(range(1,101))

for number in numbers:
	if number % 15 == 0:
		print('Fizzbuzz')
	elif number % 3 == 0:
		print('Fizz')
	elif number % 5 == 0:
		print('Buzz')
	else:
		print(number)



print(lesson_break)
print("Exercise 5-13")

# Your Ideas: Record any new ideas you may have about problems
# Cont. you might want to solve as your programming skills 
# Cont. continue to improve
# Ideas: list app (includes lists, due date)
# Cont. web app (with user input features)
# Cont. program that works with Data

