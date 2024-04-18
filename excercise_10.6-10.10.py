""" Exercise 10-6: Addition"""
"""
print("Please enter two numbers and I will add them")
print("press 'q' to quit")

number = ''

while True:
    try:
        num_1 = int(input("First number: "))
        if num_1 == 'q':
            break

        num_2 = int(input("Second number: "))
        if num_2 == 'q':
            break
        
        number_add = num_1 + num_2
        print(f"{num_1} + {num_2} = {number_add}")
    except:
        print("numbers only!")

"""

""" Exercise 10-7: Addition Calulator"""