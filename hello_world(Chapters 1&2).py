#------------------------------Chapter 1: Variables -----------------------------------
# For lesson breaks
lesson_br = "----------------------------------"
lb = "----------------------------------"
chpt_message = "CHAPTER 1"
print(chpt_message)

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

mesage = "Hello Python Crash Course reader!"
print(mesage)

print(lesson_br)

chpt_message = "CHAPTER 2"
# ------------------------------Chapter 2: Strings-------------------------------------
# Strings can be either single ('') or double quotes(")
# This allows for the use of quotes and apostrophies in strings
# Ex. 'I told my friend,"Python is my favorite language!"

# Lesson: Changing Case in a String with Methods
# NAME
print(chpt_message)

name = "ada lovelace"
print(name.title())
#title() is a method that changes each word 
#The dot(.) allows a method to act on a variable
print(name.upper())
print(name.lower())

print(lesson_br)

# Lesson: Using Variables in Strings 
#full_name

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# f-strings (f) allow insertion of variables into a string. 
# f stands for format
# use brackets around the names to replace them with their respective variables.

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)
# Another way to write it: full_name = "{}{}".format(first_name, last_name) for python 3.5 or earlier

print(lesson_br)
# Adding Whitespace to Strings with Tabs or Newlines
# tab is (\t)

print("Python")
print("\tPython")

#new line is (\n)
print("Languages:\nPython\nC\nJavascript")

#Combining tabs and new lines (\n\t)

print("Languages:\n\tPython\n\tC\n\tJavascript")

#Stripping Whitespace
#stripping white spaces from the right side of a string (rstrip()) 
# In this example white space is added to the end of the string
#NOTICE: Click on the right side of the line in the terminal to see the whitespace.
favorite_language = 'python1 '
print(favorite_language)

print(favorite_language.rstrip())

# whitespace stripping is only temporary
# To make it permentant associate the stripped value with tha variable name

favorite_language = 'python2'
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Whitespace Stripping on the left side of the string
# lstrip()

favorite_language = " python3 "
print(favorite_language.rstrip())
print(f"{favorite_language.lstrip()}left")

# Strip both sides 
# strip()

print(f"{favorite_language.strip()}both")

print(lesson_br)
print("Chapter Exercise 2.3")

#Personal Message: use a variable to represent a person's name and print a message to that person
first_name = "Mia"
message = f"Hey {first_name}, You are doing a great job!"
print(message)

print("Chapter Exercise 2.4")
#Name Cases: use a variable to represent a person's name , print that person's name in lowercase, uppercase, and title case

first_name = "Mia"
last_name = "Python"
full_name = f"{first_name} {last_name}"
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

print("Chapter Exercise 2.6")
#Famous Quote: Find a quote. Print the quote and name of author including quoation marks.

quote = "Where ever you go, there you are."
author = "Confucious"
full_quote = f'{author} once said, "{quote}"'
print(full_quote)

print("Chapter Exercise 2.6")
#Stripping names: Use a variable to represent a person's name, include white space at beginning and end of name. Use tab (\t) and new line (\n) at least once. 
#Cont. Print the name once, then print the name using each of the three stripping functions, rstrip(), lstrip(), strip()

name = ' \tlois\n '
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())

print(lesson_br)

#NUMBERS
# Integers
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2) # Exponent
print(3 ** 3)
print(10 ** 6)

#Operations
print(2 + 3*4)
print((2 + 3) * 4)

#Floats
# Any number with a decimal point
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

#Intergers and floats
print(4/2)
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

#Underscores in Numbers
universe_age = 14_000_000_000
print(universe_age)

#Multiple Assignment
# Assign values to more than one varible using just a single line
# Notice: Make sure that the spacing of each variable matches the spacing for their respective value.
x, y, z = 0, 0, 0

#Constants
# A variable whose value stays the smae thoughout the life of a program
# Constants are indicated with ALL_CAPS
MAX_CONNECTIONS = 5000
print(lb)

print("Chapter Exercise 2.8")
#Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8.

print(6 + 2)
print(10 - 2)
print(4 * 2)
print(16 / 2)


print("Chapter Exercise 2.8")
#Favorite Number: Use a variable to reprsents your favorite number. Then using that variable, create a message that reveals your favorite number. Print the message. 
favorite_number = 12
message = f"My favorite number is {favorite_number}!"
print(message)
print(lb)

# NUMBERS

# Say hello to everyone.
print("Hello Python people!")

# Python ignores anything after a hash mark (#)

#What Kind od Comments Should You Write?
#Purpose: To explain what you code is supposed to do and how you are making it work

print(lb)

# The Zen of Python
# 1. Simple is better than complex.
# 2. Complex is better than complicated.
# 3. Readability counts.
# 4. There should be one-- and preferablly only one --obvious way to do it.
# 5. Now is better than never.

print("The Zen of Python")
import this

print(lb)

