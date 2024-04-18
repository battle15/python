""" Writing to a File"""
""" 
One of the simplist ways to save data is to write it to a file
When you write text to a file, the output will still be available
after you close the terminal containing you program's output

You can examine the output after a program finishes running,
an you can share the output files with others as well.

"""
""" Writing to an Empty File"""
"""
To write text to a file, you need to call open() with a second
argument telling Python that you want to write to the file
"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Don't Stop!")


"""
The call to open() has two arguments
first argument: the name of the file we want
second argument: 'w', tells Python that we want to open the file in 
                write mode
You can open a file in read mode ('r'), write mode ('w'), 
append mode ('a'), or a mode that allows you to read and write to the 
file ('r+'). 

If you the mode argument, Python opens the file in read-only mode by default

The open() function automatically create the file you're writing to if 
it doesn't already exist. However, be careful opening a file in write mode ('w')
because if the file does exist, Python wiil erase the contents of 
the file before before returning the file object.

Then we use the write() method on the file object to write a tring to the file

"""

"""
Note: Python can only write strings to a text file. If you wnat to 
store numerical data in a text file, you'll have to convert the data 
to string format first using the str() function.

"""
#===================================================

""" Writing Mulitple Lines"""
"""
The write() function does not add newlines to the text you write.
So if you write more than one line without newline characters, your
file may not look the way you want to:

"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Don't Stop!")
    file_object.write("You are doing great!")

"""
In programming.txt the lines are squished together

"""

""" 
Including newlines in your calls to write() makes each string 
appear on its own line

"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Don't Stop! \n")
    file_object.write("You are doing great! \n")

""" 
You can also use spaces, tab characters, and blank lines 
to format your output

"""

#=============================================================

""" Appending to a File """

"""
If you want to add content to a file instead of writing over existing 
content, you can open the file in append mode. When you open a file in append more,
Python doesn't earse the contents of the file before returning the file odject.

Any lines you write to the file will be at the end of the file. If the 
file doesn't exist yet, Python will create an empty file for you..

"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("Push foward! You will get there.\n")
    file_object.write(" Don't let anything get in your way! I believe in you!\n")



