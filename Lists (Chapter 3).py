#LISTS

#Lists are a collection of items in a particular order
#Make the names of lists plural
#When making lists use squar brackets []
#Individual elements in lists are seperated by commas

lesson_break = "--------------------------------"

bicylces = ['trek','cannondale','redline','specialized']
print(bicylces)

#Accessing Elements in a list

#the index is a postion in the list, accessed by using the number of the element position in the list

bicylces = ['trek','cannondale','redline','specialized']
print(bicylces[0])

#With a method attached
print(bicylces[0].title())

#Index Positions Start at 0, Not 1
#Subtract 1 when attempting to figure out the position number
#Ex. Index is at 1 and 3

print(bicylces[1])
print(bicylces[3])

#To access the last element in a list use [-1]
#To access elements from the end of the list, use [-number position] relative to where is position from then ens of the list
print(bicylces[-1])

#Using Individual Values from a List

message = f"My first bicylce was a {bicylces[0].title()}"
print(message)

print(lesson_break)

print("Exercise 3.1")
#Names: Store the names of a few friends. Then access each name individually 

names = ['jenny', 'jan','james']
print(names[0])
print(names[1])
print(names[2])

print(lesson_break)
print("Exercise 3.2")

#Greetings: Using the names from 3.1, print a message to each person, while also printing their names. Keep the text in the message the same.

message = f"My friend {names[0].title()} rocks socks!"

print(message)

message = f"My friend {names[1].title()} rocks socks!"

print(message)

message = f"My friend {names[2].title()} rocks socks!"

print(message)

print(lesson_break)
print("Exercise 3.3")
#Your Own List: Make a list of the different types of a singular a mode of transportation. Use the list to print statements

sedans = ['honda','toyota']

message = f"I would love to have my own paid off {sedans[0].title()} one day!"

print(message)

message = f"I wonder what it would be like to drive a {sedans[1].title()}."

print(message)

print(lesson_break)

#Changing, Adding, and Removing Elements

#Modifying elements in a list
# To change an element, use the name of the list followed by the number of the element in brackets
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a list
# Appending elements to the end of a list
# use 'append' to add new items at the end of a list

motorcycles.append('ducati')
print(motorcycles)

# Adding elements to an empty list
# An empty list is represented with just '[]'  

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#an empty list is needed to collect and store the data that is appended from the an user's input

# Inserting Elements into a List 
# Insert elements using insert() and specifying the index of the new element and the value of the new item

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati') 
print(motorcycles)

#Removing Elements from a List
#Removing an Item Using the "del" Statment
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
# pop() removes an item from the end of a list, but can still be worked with after removing it.
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

#Popping items from any position in the list
# put the element number in the parenthesis of the pop() method

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)

print(f"The first motorcycle I owned was a {first_owned.title()}")

#TIP: Use the del method to remove an item without using it
#Cont. Use the pop() method to use an item as it is removed

# Removing an Item by Value
# remove()

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#remove() can also allow the removed item to be used
#However, it only removes the first occurance of the item in the list. 
#Cont. If there are more occurances, then a loop will be needed to filter out the rest

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me")


print(lesson_break)

print("Exercise 3.4")

#Guest List: Make a list of three people who you would invite to dinner. Then print a message to each person inviting them to dinner.
guest_list = ['james','jimmy','johnathan']
print(f"Hello {guest_list[0].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[1].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[2].title()}, I am officially inviting you to dinner!")


print(lesson_break)

print("Exercise 3.5")

# Changing Guest List: Someone from the guest list could not make it.  
# Cont. Add a print() call of the person who could not make it

print(f"{guest_list[2].title()} could not make it.")

# Cont. Modify the list and replace the name of the guest who could not make it with someone who can
# insert()

guest_list.insert(2,'jim')
print(guest_list)

del guest_list[3]
print(guest_list)
# Cont. Print a second set of invitation messages for each person on the list

print(f"Hello {guest_list[0].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[1].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[2].title()}, I am officially inviting you to dinner!")


print(lesson_break)

print("Exercise 3.6")

# More Guests: Add a print() call informing people that you found a bigger dinner table
# Cont. Use insert() to add one new guest in the, beginning and  middle

guest_list.insert(0,'john')
guest_list.insert(2,'jimbo')
print(guest_list)

# Cont. Use append() to add one new guest to the end of you list

guest_list.append('Jamerson')
print(guest_list)
# Cont. Print a new set of invitation messages to each person

print(f"Hello {guest_list[0].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[1].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[2].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[3].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[4].title()}, I am officially inviting you to dinner!")

print(f"Hello {guest_list[5].title()}, I am officially inviting you to dinner!")


print(lesson_break)

print("Exercise 3.7")

# Shrinking Guest List: The dinner table did not in time and now you only have space for two people

# Cont. Add a print() call informing people that you only have two spaces left

print(guest_list)
print(f"\nHello! Unfortunately, the table did not arrive in time. Therefore, there are only two spaces left")

# Cont. Use pop() to remove guest one at a time until only two guest remain 
# Cont. Each time a guest is popped from the list, print a message stating that they can no longer attend

removed_guest = guest_list.pop()

print(guest_list)


print(f"Hi {removed_guest}, you are no longer invited to dinner")

removed_guest = guest_list.pop()
print(f"Hi {removed_guest}, you are no longer invited to dinner")

removed_guest = guest_list.pop()
print(f"Hi {removed_guest}, you are no longer invited to dinner")

removed_guest = guest_list.pop()
print(f"Hi {removed_guest}, you are no longer invited to dinner")

print(guest_list)

#Print a message to the last two to let them know they are still involved

print(f"\nHi {guest_list[0]}, You are still invited")
print(f"Hi {guest_list[1]}, You are still invited")

# Cont. Use del to remove the last two name from the list. Print the list to ensure that it is empty


del guest_list[0]
del guest_list[0]

print(guest_list)

# Organizing a List
# Sorting a List Permanently with the sort() Method
# sort() puts the list in alphabetical order, however, 
# Cont. after the sort() method has been used, the list cannot revert to its original order

cars = ['bmw','audi','toyota','suburu']
cars.sort()
print(cars)

# To sort in reverse alphabetical order use "reverse = true" in the sort() method

cars.sort(reverse = True)

print(cars)

# Sorting a List temporarily with the sorted() Function
# sorted() does not affect the order of the original list

cars = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Most approaches to sorting will build directly on what is learned in this lesson.

#Printing a List in Reverse Order
# reverse() method
# The reverse() method changes the order permanently

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the Length of a List
# len() function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# len() is helpful when needing to find the amount of a list that is remaining after some items are removed

print(lesson_break)

print("Exercise 3.8")
# Seeing the World: Make a list of five places that you want to visit in a random order
places = ['Jamaica', 'Bahamas', 'Haiti','Ghana','Puerto Rico']
print(places)

# Cont. Use sorted() to print the list in alphabetical order. Print the list
print(sorted(places))

# Cont. Use sorted() to print the list in reverse alphabetical order. Print the list
# sorted() is a function, therefore identify the list and the action within it
print(sorted(places, reverse = True))

# Cont. Use reverse() to change the order of the list. Print the list

places.reverse()
print(places)

# Cont. Use reverse() to change the order again. Print the list

places.reverse()
print(places)

# Cont. Use sort() to change the list to alphabetical order. Print the list

places.sort()
print(places)

# Cont. Use sort() to change the list to reverse alphabetical order. Print the list 

places.sort(reverse = True)

print(places)

print(lesson_break)

print("Exercise 3.9")

# Dinner Guest: 

print(len(guest_list))


print(lesson_break)
print("Exercise 3.10")

#Every Function: Write a program that creates a list containing items from any category 

languages = ['english', 'spanish','french','latin','japanese']

# Cont. And then uses each funtion introduxed in this this chapter at least once
# Funtions used: 
# append()
languages.append('greek')
print(languages)

# insert()
# Should insert "Swahili" in the first position
languages.insert(0,'swahili')
print(languages)

# del

# should delete "French"
del(languages[3])
print(languages) 


# pop()

#Remove latin and print a message about the removal
language_removal = languages.pop(3)
print(f"\nThe language, {language_removal}, has been removed from the list.")

print(languages)

# remove()
#removing Spanish [2] from the list

bye_spanish = 'spanish'
language_removal = languages.remove(bye_spanish)
print(f"\nThe language,{language_removal}, has also been removed from the list")
print (languages)

# sorted()
print(sorted(languages))

# sort()
print(languages)
languages.sort()
print(languages)



# reverse = True
languages.sort(reverse = True)
print(languages)

# reverse()

languages.reverse()
print(languages)

# len()

length = len(languages)

print(f"There are {length} languages in the list.")

print(lesson_break)

# Avoiding Index Errors When Working with Lists
# Index error: List is out of range
#Tip: If an index error occurs and a solution cannot be found, try printing out the length, len(), of a list