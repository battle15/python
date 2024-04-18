""" Working with Mulitple Files """

""" 
Moving code to a function called count_words()
    This will make it easier to run the analysis 
    of multiple books

"""
''''
def count_words(filename):
    """ Count the approximate number of words in a file"""
    try:
        with open(filename, encoding= 'utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

'''

""" Try to keep comments up to date when modifying a program"""

"""
By putting the code in a function, a simple loop to count the words
in any text we want to analyze can be made

To do this, the names of the file we want to analyze are stored in a list

Then we call count_words() for each file in that list
"""
'''
def count_words(filename):
    """ Count the approximate number of words in a file"""
    try:
        with open(filename, encoding= 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
'''

"""
*siddharth.txt is purposely left out 

try-except block has two advantages
    - it prevents users from seeing a traceback
    - we can let the program continue analyzing the texts it's able to find
"""

#====================================================================

"""Failing Silently"""

"""
You do not have to report every exception that you catch

To make a program fail silently, you have to write a try block as usual
but  you explicity tell Python to do nothing in the exept block

The pass statement tells Python to do nothing in the block

"""

def count_words(filename):
    """ Count the approximate number of words in a file"""
    try:
        with open(filename, encoding= 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

""" 
The only difference between this listing and the previous one is 
the pass statement. 

Now when a FileNotFoundError is raised, the code in the except 
block runs but nothing happens

Users do not see any indication that a file was not found

pass also acts as a placeholder 
    - It reminds you that you are chosing to do nothing at a specific
    point in the programs execution and that you might to do something 
    there later 

"""

#======================================================

""" Deciding Which Errors to Report """

"""
experience will help you to know where to include exception handling blocks 
and how much to report to users

"""
