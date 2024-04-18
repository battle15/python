# Dictionaries
# Simple Dictionary
# Storing information about a particular alient
lesson_break = "==============================="

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Woring with Dictionaries
# A Dictionary is a collection of key-value pairs
# A key's value can be a number, a string, a list, or even another dictionary
# In Python, dictionaries are wrapped in brackets {}

# Key - Value pair os a set of values associated with each other 
# Every key is connected to its value by a colon
# Individual key-pairs are connected by commas

# Accessing Values in a Dictionary
# To access a dictionary
# Cont. give the dictionary name 
# Cont. then place the key inside a set of sqaure brackets

alien_0 = {'color':'green'}
print(alien_0['color'])

# Dictionaries can have an unlimited amount of key-value pairs
alien_0 = {'color':'green','points':5}

new_point = alien_0['points']
print(f"You just earned {new_point} points!")

# Adding New Key-Value Pairs
# To add a new key-value pair to a dictionary
# give the name of the dictionary followed by 
# the new key in square brackets along with the new rule

alien_0 = {'color':'green','points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an Empty Dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Typically empty dictionaries are used when storing user-supplied data
# # Or when generating a alrge number of key-value pairs automatically

# Modifying Values in a Dictionary

# To modify the value, give the name of the dictionary
# followed by the key in square brackets
# then define the new value

alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']}")

# track the position of an alien that can move at different speeds

alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print(f"Orignal position: {alien_0['x_position']}")

# Move alien to the right
# Determin how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else: 
	# The must be a fast alien.
	x_increment = 3

# The new position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


# Removing Key-Value Pairs
# the del statement complete removes the key-value pair
# use the name of the dictionary and the key that needs to be removed
# Removing "points"

alien_0 = {'color':'green', 'points':5 }
print(alien_0)

del alien_0['points']
print(alien_0)

# NOTE the deleted key-pair is removed permanently 

# A Dictionary of Similar Objects
# Store one kind of information about many objects
# When more than one line is needed to define a dictionary
# press ENTER to add a new line
# Then indent the next level one level (four spaces)
# Write the first key-value pair, followed by a comma

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}


# Look up the person based on favorite language

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Using get() to Access Values

alien_0 = {'color':'green', 'speed':'slow'}
#print(alien_0['points'])
# Returns a traceback error

# The get() method requires a key as a first argument
# As a second optional argument, you can pass the value to be 
# Cont. returned if the key doesnt exist

alien_0 ={'color': 'green', 'speed':'slow'}

point_value = alien_0.get('points','No point value assigned.')
print(point_value)

# if there is a chance that the key that you are asking for 
# Cont. does not exist, consider using the get() method
# Cont. instead of the square bracket notation

print(lesson_break)
print("Exercise 6-1")

# Person: Use a dictionary to store information about a person you know
# Store their first names, last name, age, and city where they live.
# Keys: first_name, last_name, age, city
# Print each piece of information stored

known_person = {'first_name': 'Billy', 'last_name':'boye', 'age':'29','city':'nowhere'}
print(known_person['first_name'])
print(known_person['last_name'])
print(known_person['age'])
print(known_person['city'])

print(lesson_break)
print("Exercise 6-2")

# Favorite Numbers: Use a dictionary to store people's favorite numbers
# Use five different names as keys, and a favorite number for each key
# Print each person's name and their favorite number

favorite_numbers = {
	'joe': 4,
	'jim': 5,
	'john': 6,
	'james': 7,
	'josh': 8
}

favorite_numbers = favorite_numbers['joe']
print(f"Joe's favorite number is {favorite_numbers}.")

print(lesson_break)
print("Exercise 6-3")

# Glossary
# Thing of five programming words learned in previous chapters
# Use the words as keys in the glossary
# Store their meanings as values

glossary = {
	'list':'a collection of items in a particular order',
	'loop':'program that repeats an action for every iten in a list',
	'dictionary':'a collection of key-value pairs',
	'boolean':'True or False',
	'tuple': 'an immuateble list'
}

# Print each word and its meaning as a neatly formated output 
# Print each key and value pair on a new line 

print(f"List: {glossary['list']}") 
print(f"\nLoop: {glossary['loop']}")
print(f"\nDictionary: {glossary['dictionary']}")
print(f"\nBoolean: {glossary['boolean']}")
print(f"\nTuple: {glossary['tuple']}")

print(lesson_break)

# Looping through a Dictionary
# Looping Through All Key-Value Pairs
# You can loop though a dictionary's key-value pair,
# Through its keys, or through its values

# Dictionary used to store a user's information on a website

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last':'fermi',
}

# Everything stored in a user's dictionary
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

print(lesson_break)
# To create a for loop for a dictionary,
# Create names for the two variables that will hold the key and value 
# In each key-value pair
# Then include the name of the dictionary followed by the method items()
# The method items() returns the list of key-value pairs
# for k, v in user_0.items

# looping through key-value pairs works well for dictionaries that stores
# the same kind of information for many different keys 

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

# Looping Through All the Keys in a Dictionary
# the keys() method is useful when you don't need to work with all of
# the values in a dictionary

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name in favorite_languages.keys():
	print(name.title())

# Pull all keys from the from the dictionary favorite_languages and 
# assign them one at a time to the variable

# for name in favorite_languages: produces the same output
# Send a message to specific name

print(lesson_break)
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

friends = ['phil','sarah']

for name in favorite_languages.keys():
	# Address all everyone first
	print(f"Hi {name.title()}.")
	# In the name in the list of 'friends' is the same as the name in 'favorite_languages'
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")

# If a specific person took the poll

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# Looping Through a Dictionary's Keys in a Particular Order
# This can be achieved by sorting through the for loop
# use sorted()

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

# For each name in the favorite_languages
# print list all keys in the dictionary and sort the list 
# before looping through it
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank  you for taking the poll")

# Looping Through all Values in a Dictionary
# the values() method returns the values in a dictionary
# List the languages chosen in the poll

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned:")

for language in favorite_languages.values():
	print(language.title())

#  To list values with no repeats, use set() arounr the dictionary

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
	print(language.title())

#NOTE: sets to not build a set directly usig braces and separating the elements with comma's
languages ={'python', 'ruby','python','c'}
print(languages)

# sets do not retain items in any specific order

print(lesson_break)
print("Exercise 6-4")

# Glossary 2: clean up the code from 6-3 by looping through dictionary
# items()
glossary = {
	'list':'a collection of items in a particular order',
	'loop':'program that repeats an action for every iten in a list',
	'dictionary':'a collection of key-value pairs',
	'boolean':'True or False',
	'tuple': 'an immuateble list'
}

for key, value in glossary.items():
	print(f"{key.title()}: {value}.")

print(lesson_break)
print("Exercise 6-5")

# Rivers: Make a list containing three major rivers:

rivers = {
	'Nile':'Egypt',
	'Mississippi':'U.S.A',
	'Yangtze': "China"
}

# Use a loop to print a sentence about each river
# "The Nile runs through the Egypt"

for river, country in rivers.items():
	print(f"{river.title()} runs through {country.title()}")

# Use a loop to print the name of teach river included in the dictionary
for river in rivers.keys():
	print(f"River: {river}")

# Use Use a loop to print the name of each country included in the dictionary

for country in rivers.values():
	print(f"Country: {country}")


print(lesson_break)
print("Exercise 6-6")
# Polling: Use the code in favorite_languages.py
# Make a list of people who should take the favorite poll, Include 
# some names that are already in the dictionary and some who are not

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

poll_invites = {'jen', 'phil','erin','tony','tammy'}


# Loop though the list of people who should take the poll.

for name in poll_invites:

	if name in favorite_languages:
		print(f"Hi {name.title()}, Thank you for responding to the poll")

# If they have not yet taken the poll
# print a message inviting them to take the poll
	else:
		print(f"Hi {name.title()}, Please respond to this poll")
# Nesting: 
# Used to store multiple dictionaries in a list, or a list of items
# as a value in dictionary

# You can nest dictionaries in a list, a list of item inside a 
# dictionary, or even a dictionary inside of a dictionary

print(lesson_break)

# A Listing of Dictionaries 
# Making a list of aliens in which each alien is a dictionary of 
# information about that alien

alien_0	= {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Use range() to create a fleet of 30 aliens

# Make an empty list for stoing aliens.
aliens = []

# Make 30 green aliens.
for alien_numbers in range(30):
	new_alien = {'color':'green','points':5, 'speed':'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}") 

# Change colors based and speed as time progresses
# Change the first three aliens to yellow, medium-speed aliens
# Worth 10 points each

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10

for alien in aliens[:5]:
	print(alien)

# Expand loop by with elif block that turns yellow aliens into
# red, fast-moving ones woth 15 points

# All of the dictionaries in a list should have an identical structure
# so you can loop through the list and work with each dictionary
# object in the same way

# List in a Dictionary
# Store information about a pizza being ordered

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese']
}

# Summarize the order.

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")



# running a for loop in a for loop of a dictionary 
# Store each person's responses in a list

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','hashell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s' favorite languages are:")
	for language in languages:
		print(f"\t {language.title()}")

# A Dictionary in a Dictionary

# Many_users

users = {
	'aeinstien': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'priceton',
	},

	'mcurie': {
		'first': 'marie',
		'last': 'curry',
		'location': 'paris'

	},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_time = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_time.title()}")
	print(f"\tLocation: {location.title()}")

print(lesson_break)
print("Exercise 6-7")

# People: Using the dictionary from exercise 6-1
known_person_0 = {'first_name': 'billy', 'last_name':'boye', 'age': 29,'city':'nowhere'}
# Make two new dictionaries representing different people
known_person_1 = {'first_name':'lily', 'last_name':'smith', 'age':43, 'city':'here'}

known_person_2 = {'first_name':'jill','last_name':'mac', 'age':32, 'city':'there'}

# Store all three dictionaries in a list called people

people = [known_person_0,known_person_1,known_person_2]

# Loop through the list

for person in people:

# Print everthing you know about the person	
	print(person)

print(lesson_break)
print("Exercise 6-8")

# Pets:  Make serveral (3) dictionaries, 
# Where each dictionary represents a different pet
# Include the kind of animal and the owner's name
pet_0 = {'type':'cat','owners_name':'megan'}
pet_1 = {'type':'dog','owners_name':'jake'}
pet_2 = {'type':'horse', 'owners_name':'rick'}
pet_3 = {'type': 'rabbit', 'owners_name':'jessica'}

# Store these dictionaries in a list called pets

pets =[pet_0, pet_1, pet_2, pet_3]

# Loop though the list and print everthing you know about the pet 

for pet in pets:
	print(pet)

print(lesson_break)
print("Exercise 6-9")

# Favorite Places: Make a dictionary of called favorite places:
# Use three names as keys 
# store one to three places for each person
favorite_places = {
	'nancy': ['greece','spain'],
	'rene': ['tokyo', 'london'],
	'hank': ['dallas'],
	'ron': ['brazil','nigeria','egypt']
}


# Loop through the dictionary 

for name, place in favorite_places.items():
# Print each person's name and favorite places	
	print(name)
	print(place)


print(lesson_break)
print("Exercise 6-10")

# Favorite numbers: Modify the program from 6-2
# so that each person can have more than one favorite number

favorite_numbers = {
	'joe': [4,8],
	'jim': [5,6,29],
	'john': [6,80,23],
	'james': [7,20],
	'josh': [8, 48]
}

for name, numbers in favorite_numbers.items():
	print(f"{name}'s favorite numbers are:")
	for number in numbers:
		print(f"{number}")
# print each person's name along with theit number

print(lesson_break)
print("Exercise 6-11")

# Cities: Make a dictionary called cities
# Use the names of three cities as keys 
# create a dictionary about each city:
# Include: country, approximate population, one fact about the city
# keys for each city: country, population, fact

cities = {
	'nadao' :{
		'country':'nadaland',
		'population': 12_999,
		'fact': 'made up of cheese'
	},
	'mazco' : {
		'country':'mazland',
		'population': 122,
		'fact': 'it appears every 9 years'
	},
	'simco' : {
		'country' :'simland',
		'population': 400_444_323,
		'fact': 'home of the largest cow'
	}
}

# print the name of each city and all of the information stored for it

for city, city_info in cities.items():
	print(city.title())
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']

	print(f"\t{country.title()}")
	print(f"\t{population}")
	print(f"\t{fact}")

print(lesson_break)
