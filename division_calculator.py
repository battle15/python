"""Execeptions"""

"""
In Python, execptions manage errors that arise during a program's 
execution
Whenever an error occurs that makes Python unsure what to do next,
it creates an exception object.
If you write code that handles the execptionn the program will 
continue running.
If you don't handle the exeption the program will halt and 
show a traceback, which includes a report of the exception

Exceptions are handled with try-except blocks
    A try-except block asks Python to do something, but it 
    also tells Python what to do if an execption is raised 
        Instead of seeing tracebacks, users will see friendly 
        error messages that you write 

"""

""" Handling the ZeroDivsionError Exception"""

# print(5/0)
# returns an error

""" Using try-except Blocks"""
"""
When you think an error may occur, you can write a try-except block
to handle the exception that might be raised.

You tell Python to try running some code, and you tell it what to 
do if the code results in a particular kind of exception

"""

try:
    print(5/0)

except ZeroDivisionError:
    print("You can't divide by zero!")

""" 

If the code in the try block works, then Python skips over 
the exception block.

If the code in the try block cause an error, Python looks
for the an except block whose error matches the one that 
was raised and runs the code in that block

If more code followed the try-except block, the program
would continue running because we told Python how to handle
the error

"""

""" Using Exceptions to Prevent Crashes"""

""" 
If a program repsonds to invalid input apprppriately, it can prompt
for a more valid input instead of crashing
"""
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
"""

""" 
Because this program does nothing to handle errors,
asking it to divide by zero causes it crash.

It is not good to let users see traceback errors
Nontechnocal users: will be confused by them
attackers: will learn more than you want them to know froma
            a traceback
            Ex. They will know the name of the program file
            and they will see a part of your code that isnt working
            properly.

            A skilled attacker can sometimes use this information to
            determine which kind of attacks to use against your code

"""

#===========================================================

""" The else Block """

"""

A program can be made more resistant by wrapping the line that might 
produce errors in a try-except-block

with an else block, Any code that depends on the try block executing 
successfully goes in the else block


"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
        
    except ZeroDivisionError:
        print("You can't diving by 0!")

    else:
        print(answer)

    """
    
    We ask Python to try to complete the division operation in a 
    try block, which includes only the code that might cause and error.
    Any code dependent on the try block succeeding is added to 
    the else block 

    except: Tells Python how to respond when a ZeroDivisionError arise

    """

    """
    try-except-else block explanation

    Python attempts to run the code in the try block. 
        Only code that might raise an exception

    code that should run if the try block is successful 
    goes in the else block

    The except block tells Python what to do in case a certain 
    exception arises when it tries to run the code in the try block


    
    """




