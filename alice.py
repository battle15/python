""" Handling the FileNotFound Exception"""

"""
involves handeling missing files

"""
"""
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f. read

# An exception is raised

"""

"""
1. the variable ,f, to represent the file object, 
which is a common convention 

2. the encoding argument is needed when a system's default encoding
doen't match the encoding of the file that's being read

In this example, the open() function produces the error, so to 
handle it, the tryblock will begin with the line contains open()"
"""
"""
filename = 'alice.txt'

try:
    with open(filename, encoding= 'utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
"""

""" Analyzing Text """

"""
The texts used in this section come from Project Gutenberg 
    link: (https://gutenberg.org/)

    This example works with Alice in Wonderland

Try to count the number of words in the text

use the string method split(), which can build a list of 
words from a string

"""
title = "Alice in Wonderland"
print(title.split())

"""
split() method separates a string into parts whenever it finds
a space and stores all the parts of the string in a list

"""

filename = 'alice.txt'

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

"""
The file has now been moved to the correct dictory
We now take string contents, which now contains the entire
text of Alice i Wonderland as one string and use split() 
method to produce a list of all the words in the book

len() is used to examine the list and get an approximation 
of the number of words in the original string

Then a statement about the number of words found in the file are printed
"""
