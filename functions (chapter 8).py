# Functions

import archived_functions as af
import archived_functions
from archived_functions import show_messages
from pizza import make_pizza as mp
from pizza import make_pizza
lesson_break = '=================='

# Functions are named blocks of code that are designed to do one specific job
# Calling functions allows Python to run the code within the function

# Defining a Function
# function that prints a greeting


def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()

# The keyword def defines a function. This is the function definition
# The parentheses holds the information that function needs to do its job
# A function call tells Python to execute the code in the function
# To call the function write the name of the function
# followed by a parentheses . 'greet_user()'

# Passing Information to Function

# To greet the user by name in a fuction
# enter 'username' in the parentheses of a
# function's definition at greet_user()
# This allows the function to accept the value of username that is specified
# The function now expects a value for username to be
# provided everytime it called

# When greet_user() is called, a name such as 'jesse' can be provided

'''
def greet_user(username):
    print(f"Hello, {username.title()}")
greet_user('jesse')

'''

# Argument and Parameters

# The variable, username, is an example of a parameter
# A parameter is a piece of informatino the function needs to do its job
# The value 'jesse' in greet_user('jesse') is an example of an argument
# An argument is a piece of information
# that's passed from a function call to a function
# When a function is called, we place the vlause we want the function
# to work with in parentheses

print(lesson_break)
print('Exercise 8-1')
# Message: Write a function called display_message() that prints what
# you are learning about

'''
def display_message():
    print("I am learning about functions")
display_message()
'''

print(lesson_break)
print('Exercise 8-2')
# Favorite Book:

'''
def favorite_book(title):
    print(f"One of my favorite book titles is called {title.title()}")
favorite_book('Panchinko')

'''
# Passing Arguments
# Passing multiple arguments
# Some ways to pass arguments:
# Postitional arguments need to be in the
# same order the parameters are written
# Keyword arguments, each argment consists of a variable name
# and a value
# List and dictionaries of values

# Positional Arguments

'''
def describe_pet(animal_type, pet_name):
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')
'''

# the order of the arguments in the function call
# must be the same as the order of the parameters in the function's definition

# Multiple Function Calls
# functions can be called as many times as needed

'''
def describe_pet(animal_type, pet_name):
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')
describe_pet('dog','willie')
'''
# Calling a function multiple times is a very efficient way to work
# In this case, anytime you want to describe a new pet,
# you call the function with the new pet's information

# Order Matters in Positional Arguments

'''
def describe_pet(animal_type, pet_name):
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('harry','hamster')
'''

# Keyword Arguments

# A keyword argument is a name-value pair that you pass to a function
# Directly associate the name and the vakue within the argument
# This prevents confusion
# This also free you from having to worry about correclty ordering your
# arguments ina function call

'''
def describe_pet(animal_type,pet_name):
        print(f"\nI have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(animal_type = 'hamster', pet_name ='harry')
'''
# When using keyword arguments BE SURE to use the exact names
# of the parameters in the function's definition

# Default Values
# If an argument for a parameter is not provided,
# Pythong uses the parameter's default value
# Using default values can simplify your function calls and clarify
# the ways in which your functions are typically used
# Setting the default animal to 'dog'


def describe_pet(pet_name, animal_type='dog'):
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='willie')


# 'dog; is included as the default value in te parameter
# animal_type = 'dog'
# The order of the parameter still matter.
# The default value for animal_type makes having an argument for it unnecessary
# But, Python will still use it as the first argument
# in function its position is not changed

# The simpliest way to use the function now is to provide just
# the dog's name
'''describe_pet('willie)'''
# To call this function for a different animal,
# explictly change the animal_type with a keyword argument
''' describe_pet(pet_name = 'harry', animal_type = 'hamster' )'''
# This will call python to ignore the default value

# ANY PARAMETER WITH A DEFAULT VALUE NEEDS TO BE LISTED
# ALL THE PARAMETERS WITHOUT DEFAULT VALUES


# Equivalent Function Calls
# Avoiding Argument Errors:
# Make sure that the number of arguments in the function call
# matches the number of parameters in the functions definition

print(lesson_break)
print("Execise 8-3")
# T-Shirt:
# print size and message of t-shirt
# call function eith positional arguments
# and keyword arguments

'''
def make_shirt(size,message):
    print(f"T-Shirt size: {size.title()} ")
    print(f"Message: {message}")

make_shirt('medium','don"t give up!')
make_shirt(size = 'large', message = 'A job is at the end of this!')

'''
print(lesson_break)
print("Execise 8-4")

# Large Shirts:
# large shirts with a
# default message = " I love python"
# large and medium sizes shirts with default message
# shirt of any size with different message

'''
def make_shirt(size, message = 'I love Python'):
        print(f"T-Shirt size: {size.title()} ")
        print(f"Message: {message}")
make_shirt('large')
make_shirt('medium')
make_shirt('small', message = 'push through!')

'''

print(lesson_break)
print("Execise 8-5")
# Cities:

'''
def describe_city(city,country = "united states"):
    print(f"{city.title()} is in {country.title()}.")
describe_city('chicago')
describe_city('new york')
describe_city('ontario', country = "canada")
'''

# ============================================

# Return Values
# The return statement takes a value from inside a function
# and sends it back to the line that called the function
# Return values allow you to move much of your program's
# grunt work into function, which simplify the body of your program

# Returning a Simple Value

'''
def get_formatted_name(first_name, last_name):
    # Return a full name, neatly formatted
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

'''

# When you call a function that returns a value,
# you need to provide the variable that the return value can be assigned to
# In larger programs Return values are useful because you can store the values
# seperately and then call the function when needed

# Making an Argument Optional
# To make an argument optional give the argument an empty default value
# and ignore the argument unless the user provides a value


'''
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee','hooker')
print(musician)

'''

'''
def get_formatted_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
'''
'''
# Returning a Dictionary 

# The following funtion takes in part of a name and 
# returns a dictionary representing a person

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

'''

'''
# Store a person's age as well
def build_person(first_name, last_name, age=None):
    person = {'first':first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

'''
# The special value 'None' is used when a variable
# has no specific value assigned to it
# 'None' can be seen as a placeholder value
# In conditional test, None equates to False

# Using a Function with a while Loop

'''
def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print(f"\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
'''

'''
# Adding a break option

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print(f"\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
'''

'''
# =========================================================
print(lesson_break)
print("exercise 8-6")
# City Names:


def city_country(city, country):
    """Return city and country neatly formatted"""
    msg = f"{city}, {country}"
    return msg.title()


city_name = city_country('chicago', 'illinois')
print(city_name)

city_name = city_country('tokyo', 'japan')
print(city_name)

city_name = city_country('mexico city', 'mexico')
print(city_name)

print(lesson_break)
print("exercise 8-6")

'''

# Album:

'''
def make_album(artist_name, album_title, song_number=None):
    """Return a dictionary containing the artist name and album title"""
    album = {'artist': artist_name, 'title': album_title}
    if song_number:
        album['number of songs'] = song_number
    return album


album_info = make_album('betty', 'the best of betty')
print(album_info)

album_info = make_album('lenny', 'my songs')
print(album_info)

album_info = make_album('han', 'hans solos')
print(album_info)

album_info = make_album('sza', 'ctrl', song_number=17)
print(album_info)

'''
'''
print(lesson_break)
print("exercise 8-7")
# User Albums:

def make_album(artist_name, album_title, song_number=None):
    album = {'artist':artist_name, 'title':album_title}

    if song_number:
        album['number of songs'] = song_number
    return album

while True:
    print("\nEnter the name of the artist")
    print("(enter 'q' to quit at any point)")

    a_name = input("Artist: ")
    if a_name == 'q':
        break

    print("\nEnter the title")
    title = input("Title: ")
    if title == 'q':
        break

    formatted_name = make_album(a_name, title)
    print(formatted_name)
'''
# Passing a List
# When you pass a list to a function,
# the function get direct access to the contents if the list
'''
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanna','ty','margot']
greet_users(usernames)
'''

# Modifying a List in a Function
# Any changes made to the list inside of a function's body are permanent
# this is useful when working with large amounts of data

# Without functions

'''
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print(unprinted_designs)
print(completed_models)

'''

# Organizing the code into seperate functions

'''
def print_models(unprinted_designs, completed_models):

    # Simulate printing each design, until none are left
    # Move each design to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_model):
    # Display all completed models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Body of the program
# Easier to read


unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''

# This technique is more efficient than having to update code
# seperately in serveral places in the program
# Every code should have one specific job
# You can always call a function from another function

# Preventing a Function from Modifying a List
# If you wanted to keep the original list of unprinted designs
# instead of emptying out the list
# Send a copy of a list to a function:
'''function_name(list_name[:])'''
# The slice notation [:] makes a copy of the list to send to the function
'''print_modles(unprinted_designs[:], completed_models)'''
# The function will fill the list completed_models
# with the names from the unprinted_designs list
# but, the orignal unprinted_designs list will be unaffected

print(lesson_break)
print("exercise 8-9")
# Messages

'''
def show_messages(texts):
    """Print each text message"""
    for text in texts:
        print(text)

text_messages = ['hey', 'whats up?', 'how are you?']
show_messages(text_messages)
'''

print(lesson_break)
print("exercise 8-10")

# Sending Messasges

'''
def show_messages(texts, sent):
    
    while texts:
        removed_text = texts.pop()
        sent.append(removed_text)

        # print(text)


text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages, sent_messages)

print(text_messages)
print(sent_messages)

'''
print(lesson_break)
print("exercise 8-11")

# Archived Messages

'''
def show_messages(texts, sent):

    while texts:
        removed_text = texts.pop()
        sent.append(removed_text)

        #print(text)


text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)

'''

# Passing an Arbitrary Number of Arguments
# If you do not know how many arguments to pass ahead of time
# *parameter collects as many arguments as a the calling line provides

'''
def make_pizza (*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
'''

# an asterisk in the parameter name *toppings
# tells python to make an empty tuple (immutable list) called toppings and pack whatever
# values it recieves into this tuple

# replace the print() call with a loop that runs through the list of toppings
# and describes each one

'''
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

# This syntax works no matter how many arguments the function receives

# Mixing Positional and Arbitrary Arguments
# Python matches positional and keyword arguments first and
# then collects any remaining arguments in the final parameter

'''
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    print(f"\nMaking a {size}-inch pizza with the following topping")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(13, 'mushrooms', 'green peppers', 'extra cheese')
'''

# Using Arbitrary Keyword Arguments
# If you do not know what kind of information will be passed to the function
# Building a user profile: first name, last name, everything else

'''
def build_profile(first, last, **user_info):
    """Build a dictionary containg eveything we know about a user."""
    # Add the first and last names to user_info dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')

print(user_profile)

'''

# The double asterisks (**) before the parameter **user_info
# cause Python to create an empty dictionary called user_info and
# pack whatever name-value pairs it receives in this dictionary

# You'll oftem see the parameter name **kwargs used to collect non-specific keyword arguments

print("exercise 8-12")
# Sandwiches

'''

def sandwich(*toppings):
    print(f"\nToppings on sandwich:")

    for topping in toppings:
        print(f"-{topping}")


sandwich('lettuce', 'cheese', 'tomatoes')
sandwich('cheese')
sandwich('apples', 'chicken')

'''

print("exercise 8-13")
# User Profile:

'''
def build_profile(first, last, **user_info):
    """Build a dictionary containg eveything we know about a user."""
    # Add the first and last names to user_info dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'mia', 'python', location='chicago', field='information technology', age=27)

print(user_profile)
'''
'''
print("exercise 8-13")
# Cars:

def build_car(manufacture, model, **car_info):
    """Store information about a car in a dictionary"""
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info

cars = build_car('toyota','camry', color='blue', tow_package=True)

print(cars)
'''

# Storing Your Functions in Modules
# Modules are seperate files that can hold functions and be imported
# An import statement tell Python to make a code in a module available
# in the currently running program

# Storing functions in seperate files allows you to hide
# the details of your program's code and focus on the higher logic
# While in modules, these functions  can be shared with other programmers
# There are two ways to import modules:

# Importing an entire module
# Creating a module
# A module is a file ending in .py that contains the code you want to
# import into your program

# function has been copied to "pizza.py"
# file must be in the same directory

'''
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
'''
# -----
'''
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')
'''

# To call a function from an imported module,
# enter the name of the module you imported, pizza,
# followed by the name of the function, make_pizza,
# seperated by a dot
"""pizza.make_pizza"""

# =========================================

# Importing Specific Functions
# General sytax for this approach
"""from module_name import function_name"""

# Many functions can be imported
# by seperating each function's name with a comma

"""from module_name inport function_0, function_1, function_2"""

'''
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''

# Becuase the specific function was inported, it can be called by name
# A dot notation is not needed

# =================================================

# Using as to Give a Function an Alias

# When a name of a function from a module is too long or
# conflicts with an existing name in your current program
# give it an alias (a unique nickname) as you import the function

'''
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
'''

# The import statement renames the function.
# Now anytime we want to call the function, make_pizza
# # we can just use the alias, mb
# General synax for providing an alias

"""from module_name import function_name as fn"""

# =====================================================

# Using as to Give a Module an Alias
# This can make calling the module more concise

'''
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers',' extra cheese')

'''

# The module has been given an alias, but the function names are the same
# General syntax for this approach

""" import module_name as mn"""

# ======================================================


# Importing All Functions in a Module

# Import every funtion in a module using the asterisk (*) operator

'''
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers',' extra cheese')
'''
# Because every function is imported,
# you can call each function by name without using the dot notation

# However, it's best to not use this approach when you are working
# with larger modules that you did not write
# If the module has function names that matches an existing name
# in your project, you can get some unexpected results

# Cont. Instead of importing all the funcstions seperately
# Python will overwrite the functions


# The Best approach is to import the function or functions that you want
# Or import the entire module and use the dot notation

# ======================================================

# Styling Functions
# Functions should have descriptive names
# Funcation names should use lowercase letter and underscores

# Every function should have a comment that
# explains concisely what the function does
# This comment should appear immediatley after the function definition
# and use the docstring format
# If you specify a default value for a parameter,
# no spaces should be used on either side of the equal sign

"""def function_name(parameter_0, paramter_1='default value')"""
# The same convention should be used for keywork arguments in function calls
"""function_name(value_0, parameter_1='value)"""

# Limit lines of code to 79 characters
# If a set of parameters causes a function's definition to be longer
# than 79 characters.
# Press ENTER after the opening parenthesis on the definition line.
# On the next line, press TAB twice to separate
# the line of arguments from the body of the function

"""def function_name(
            parameter_0, parameter_1, parameter_2,
            parameter_3,parameter_4,parameter_5):
        function body...
"""
# Seperate functions by two lines to make it easier to see
# where one function ends and where the next one ends

# All import functions should be written in the at the beginning of a file

# ==============================================================

# EXERCISE 8-15
# Printing Models


# printing_models.py copied to printing_functions.py

'''
def print_models(unprinted_designs, completed_models):

    # Simulate printing each design, until none are left
    # Move each design to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_model):
    # Display all completed models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Body of the program
# Easier to read


unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''
'''
import printing_functions

printing_functions.show_completed_models
'''

# ===========================================================

# Execise 8-1
# Imports

# module name: archived_functions,py
'''
def show_messages(texts, sent):

    while texts:
        removed_text = texts.pop()
        sent.append(removed_text)

        #print(text)


text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)

'''

'''
text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

archived_functions.show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)
'''

# ===
'''
from archived_functions import show_messages

text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)
'''

# ===
'''
from archived_functions import show_messages as sm

text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

sm(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)
'''

# ===

'''
text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

af.show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)
'''

# ===
'''
from archived_functions import *

text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)

'''