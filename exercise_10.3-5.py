"""Exercise 10-3: Guest"""

"""

filename = "guest.txt"
name = input("What is your name? ")


with open(filename, 'w') as file_object:
   

    file_object.write(name.title())

"""
#===================================

"""Exercise 10-4: Guestbook"""


"""
filename = 'guest.txt'

prompt = "What is your name? "
name = ''

while name != 'q':
    name = input(prompt)
    

    with open(filename,'w') as file_object:
        file_object.write(f"\nHi {name}!")

"""
#===============================================

"""Exercise 10-5: Programming Poll"""
filename = "responses.txt"

prompt = "Why do you like programming?"
response = ''

while response != 'q':
    response = input(prompt)

    with open(filename, 'a') as file_object:
        file_object.write(f"\n{response}")

