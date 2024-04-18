# Reading Line by Line
# You can use a for loop on the file object examine each line from
# a file one at a time:

'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
'''

# We assign the name of the file we're reading from to the variable 
# filename
    # This is a common convention when working with file
# After we call open(), an object representing the file and its contents
# is assigned to the variable file_object
# We use the 'with' syntax to let Python open and close the file properly
# to examine the file's contents, we work through each line in the file 
# by looping over the file object
    # When we print each line, we find even more blanks

# The blank lines are appear because an invisibl newline character is 
# at then end of each line in the text file

# The print() function adds its own  newline each time we call it,
# so we end up with two newline characters at the end of each line:
    # One from the file line and from print(). 
    # Using rstrip() on each line in the print() call eliminates these
    # extra blank lines

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
""""
When you use 'with; the file object returned by open() is only available 
inside the block that contains it,

If you want to retain aceess to a file's contents outside the with block,
you can store the file's lines in a list inside the block then wotk with
that list

    You can process parts if the file immediately and postpost some 
    processing for later in the program

"""
# The following example stores the lines of pi_digits.txt in a list
# inside the with block and then prints the line outside the with block:

""" Working with a File's Contents"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # rstrip() removes the white space on the left side of the line
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

"""
We start by opening the file and storing each line of digits in a list.
We then create a variable, pi_string, to hold the digits of pi.
We then create a loop that adds each line of digits to print this 
string and also show long the string is:
"""

"""
Note: When Python read a file, it interpretes all of the content as a 
    string. If you read in a number and want to work with that value
    in a numerical numerical context, you'll have to convert it to an
    integer using the int() function or convert it to a float using the
    float() function
"""

#============================================================

"""Large Files: One Million Digits"""

""" Printing the first 50 decimals of pi"""

filename ="pi_million_digits.txt"

with open(filename) as file_object:
    """readlines() method takes each line from the file and stores it
       a list.
    """
    lines = file_object.readline()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

#==============================================================

"""
Is Your Birthday Contained in Pi?

"""

filename ="pi_million_digits.txt"

with open(filename) as file_object:
    """readlines() method takes each line from the file and stores it
       a list.
    """
    lines = file_object.readline()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:  
    print("Your birthday do not appear in the first million digits of pi")

