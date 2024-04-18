
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

    print(contents)
'''


# open() function allows the file to be opened to work on it
# open() needs one argument: the name of the file you want to open
# python looks for the file in the directory where the program 
# that is currently being executed it stored
# file_reader.py is running, therefore, Python looks for py_digits.txt
# in the directory wehere file_reader.py is running

# open() returns and object representing  the file.
# open('pi_digits.txt') returns an object representing pi_digits.txt 
# Pything assigns this object to file_object

# The Keyword 'with' closes the file once access to it is no longer needed.
# A file can be closed with the close() method, but if a bug 
# in the program prevents close() method from being executed, 
# the file may never close.

# Improperly closed files can cause data to be lost or corrupted
# If you call close() too early on a file, you'll be working with 
# a closed file (a file you can't access), which leads to 
# more errors.

# with the structure presented in this program, it can be trusted 
# that Python will figure out when to close the file for you
# Python will automatically close the file when the 'with' block 
# finishes execution 

# Once we have a file object representing pi_digits.txt 
# we use the read(method) in the second line of program 
# to read the entire contents of the file and 
# store it as one long string in contents

# They only different between this and output and the original file 
# is the extra line at the end of the output
# The blank line appears because read() returns an empty string
# when it reaches the end of the line.
# To remove the extra line, use strip() in the call to print()

with open('pi_digits.txt') as file_objects:
    contents = file_objects.read()

print(contents.rstrip())

#=======================================================

# File Paths
# Sometimes, the file you want to open wont be in the 
# same directory as your program file
# Program might be stored in a folder called, python_work
# but inside the python_work folder could be 
# text files could be stored in a folder caled text_files
# To get python to open files from a directory other than 
# the one where your program file is stored, 
# you need to provide a file path, which tells Python to 
# look for a given location on your system

# Becuase the file path is inside python_work, you can use
# a relative path to open a file from text_files
# A relative file path tells Python to look for a given location
# relative to the directory where the currently running program file
# is stored. 

""" with open('text_files/filename.txt') as file_object: """
# This lines tells Python to look for the desired .txt file 
# in the folder text_files and assumes that text_files is located inside
# python_work (which it is)

# Window systems use backslash (\) instead of a forward slash (/) 
# when displaying file paths

# You can tell Python exactly where the file is on your computer 
# regardless of where the program that's being executed is stored
# this is called an absolute path
# You use an absolute path if a relative path doesn't work
# Absolute paths are usually longer than relative paths, 
# so its helpful to assign them to a variable and 
# then pass that variable to open():

"""
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_objects:
"""
# Using absolute paths you can read from any location on your system

# Note: you try to use backslashes in a file path, 
# you'll get an error becuase the backslash is used to escape 
# characters in strings (i.e. '\t' or '\n')
# If you need backslashes, you escape each one in the path
""""C:\\path\\to\\file.txt"""

#==============================================================







