# User Input and While Loops
# How the input() Function Works
# The input() funtion pauses the program and waits for the user
# to input some text. the input is then assigned to a variable

lesson_break = "=================================="

   #message = input("Tell me something, and I will repeat it back to you:")
   #print(message)

# Writing Clear Prompts
# Include clear and easy-to-follow prompts that tell the users
# exactly what kind of informatino you're looking for

   #name = input("Please enter your name: ")
   #print(f"\nHello, {name}!")

# Writing a prompt that is longer than one line

''''
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}")
'''
# Using int() to Accept Numerical Input
# The int() function tells Python to treat the input as a numerical value

''''
age = input("How old are you?")

age = int(age)
print( age >= 18) 
'''

# Determine whether people are tall enough to ride a roller coaster:

''' 
height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're a little older") 
'''
# The Modulo Operator
# The modulo operator (%) divides one number by another number and returns the remainder:

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

# The modulo operator doesn't tell how many times one number fits
# into another number, just what the remainder is

# Even or odd?
# Even numbers are always divisible by 2

''''
number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd.")

'''

print(lesson_break)
print("Exercise 7-1")
# Rental Car: Write a program that asks the user what kind of rental 
# car the would like.
# Print a message about that car.

''''
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}")
'''
print(lesson_break)
print("Exercise 7-2")
# Restaurant Seating: Write a program that asks the user 
# how many people are in their dinner group
# If the table is more than eight, 
# say that they will have to wait for a table
# Otherwise, their table is ready

''''
group_amount = input("How many people are in your group? ")
group_amount = int(group_amount)

if group_amount > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")
'''

print(lesson_break)
print("Exercise 7-3")
# Muliples of Ten: Ask the user for a number
# Then report whether the number is a multiple of 10 or not
# x % 10 

'''
number = input("Please enter a number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print (f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

'''
print(lesson_break)
# Introducing while Loops
# while loops run as long as, or while, a certain condition is true

# The while Loop in Action
# Count through a series of numbers

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit

'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message )

'''
# The variable 'message' is defined to track whatever value the user enters
# message is defined as an empty string "", so that Python has something to 
# check the first time it reaches the while statement

# In the loop, message is defined as the user's input
# As long as the user's input is not 'quit', 
# then the program will continue running

# To remove the 'print' output, 
# print a message instead using an if statement

'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    # message only prints if it does not match the quit value
    if message != 'quit':
        print(message )

'''

# Using a Flag
# a flag variable acts as a signal to the program

'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
'''

# The program starts in an active state (active = True)
# while statement is simplier becasue no comparison is made 
# in the while statement
# as long as the active variable remains True, the program will keep running
# If the user enters 'quit', we set active to False, and the loop stops
# 
# This makes it easier to add more tests (elif statements) 
# for events that could cause active to become False
# i.e different conditions that would cause a game or program to end

# Using break to Exit a Loop
# Use a break statement to exit a while loop immediately regardless 
# of the results of any conditional test
# break statements direct the flow of the program
# they can be used to control which lines are executed and which arent

'''
prompt = "\nPlease enter the name of a city you have visted"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")
'''

# A loop that starts with 'while True' 
# will run forever until it reaches a break statement
# Note: break statements can be made in any of Python's loops
# Ex. A break statement in a for loop that is running through dictionaries

# Using continue in a loop
# You can use the continue to return to the beginning of the loop 
# based on the result of a conditional test
# Ex. Loop counts from 1 to 10 but prints only odd numbers

'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)  

'''

# Avoiding Infinite Loops
# Every while loop needds a way to stop running 
# so it wont continue to run forever

x = 1 
while x <= 5:
    print(x)
    x += 1

# If (x += 1) is removed the loop will run forever
# The value willl start at 1 and never change
# If an infinite loop happens press CTRL- C 
# OR just close the terminal window displaying the program's output

print(lesson_break)
print("Exercise 7-4")
# Pizza Toppings: Write a loop that prompts the user to enter a series 
# of pizza toopings until they enter a 'quit' value
# As they enter their pizza topping
# print a message saying that you'll add the topping to the pizza

'''
prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'quit' when you are finished. ")
message = ""

while (message) != 'quit':
    message = input(prompt)
    print(f"\n{message} will be added to your pizza")

'''

print(lesson_break)
print("Exercise 7-5")
# Movie Tickets: A movie theater charges different ticket prices 
# depending on a person's age
# under 3 = free
# between 3 and 12 = $10
# over 12 = $ 15
# write a loop that asks for the user's age and 
# then tells them the cost of their movie

'''
prompt = "Please enter your age for your ticket cost: "

age = input(prompt)
age = int(age)



if age < 3:
    print("\n Ticket cost: free")
elif age <12:
    print("\nTicket cost: $10")
else:
    print("\nTicket cost: $15")

'''

print(lesson_break)
print("Exercise 7-6")

# Three Exits: Write the different versions of either Excercis 7-4 or 7-5
# that do each of the following:
# Use a conditional test in a while statment to stop the loop
'''
prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'quit' when you are finished. ")
message = ""

while (message) != 'cheese':
    message = input(prompt)
    print(f"\n{message} will be added to your pizza")

'''
# Use an active variable to control how long the loop run

'''

prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'quit' when you are finished. ")
message = ""
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"\n{message} will be added to your pizza")
'''

# Use a break statement to exit the loop when the user enters a 'quit' value

'''
prompt = ("\nPlease enter the pizza topping that you will like.")
prompt += ("\n Please type 'quit' when you are finished. ")
message = ""

while True:
    message = input(prompt)
    if (message) == 'quit':
        break
    else:
        print(f"\n{message} will be added to your pizza")
    
'''

# Using a while Loop with Lists and Dictionaries
# A for loop is effective for looping through a list
# To modify a list as you work through it use a while loop
# Using while loops with list allows you to 
# collect, store, and organize lots of input to examine and report later

# Moving Items from One List to Another
# Use a while loop to pull users from one list of unconfirmed users
# as we verify them and then add them to a seperate list of confirmed users
# 
# Start with users that need to be verifiied,
# and an empty list to hold confirmed users:
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

'''
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print ("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(confirmed_users)

'''

# Removing All Instances of Specific Values from a List
# removing all instances of 'cat'

'''
pets = ['dog', 'cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''
# Filling a Dictionary with User Input
# Polling program that passes the loop prompts for the participant's 
# name and response
# store the gathered data in a dictionary

'''
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday?" )

    # Store the response in a dictionary.
    responses[name] = response

    # Find out if anyone else is going to take a poll

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

'''

print(lesson_break)
print("Exercise 7-8")
# Deli: Make a list called sandwich_orders 
# and fill it with the names of various sandwiches

'''
sandwich_orders = ['ham','chicken','turkey','veggie']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each order
# As each sandwich is made, move it to the finshed_sandwiches list
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

# After all sandwiches have been made,
# print a message listing each sandwich that was made
for sandwich in finished_sandwiches:
    print (f"\nI made your {sandwich} sandwich!")
print(finished_sandwiches)
    
'''


print(lesson_break)
print("Exercise 7-9")
# No Pastrami: Using the list of orders from 7-8, 
# make sure 'pastrami' is on the list three times
# Add near the beginning of the program to print a message saying 
# the deli has run out of pastrami
# Use a while loop to remove all instances of 'pastrami' from sandwich_orders
# Make sure no pastrami sandwiches end up in finished_sandwiches

'''
sandwich_orders = ['ham','pastrami','chicken','pastrami','turkey','pastrami','veggie']

finished_sandwiches = []

print("The deli has run out of pastrami")

# Removing pastrami from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)


for sandwich in finished_sandwiches:
    print (f"\nI made your {sandwich} sandwich!")
print(finished_sandwiches)
'''

print(lesson_break)
print("Exercise 7-10")
# Dream Vacation: Write a program that polls users about their dream vacation
# Write a prompt
# Include a block of code that prints the results of a poll

'''
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt"
    name = input("What is you name? ")
    response = input("What is the location of your dream vacation? ")

    responses[name] = response

    repeat = input("Any more responses? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to go to {response}.")

'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{full_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)