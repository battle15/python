# Classes

# When you write a class, you define the genreal behavior
# that a whole catgory of objects can have
# Making an object from a class is call instantiation,
# and you work with instances of a class

# Creating and Using a Class
# Creating the Dog Class
# Each instance created from the Dog class will store a name and an age
# and we'll give each dog the abilty to sit() and roll_over()
'''
class Dog:
    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialiize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")

'''
# CLASS
# defined by capitalized names
# There are not parentheses in the class definition
# because it is being made from scratch
# Write a docstring describing what the class does

# THE __init__() METHOD
# A function that is a part of a class is a method
# The __init__ () method has two leading underscores and two trailing underscores
# This method runs automatically whenever a new instance is created
# based on the class that it is in.
#  The self argument is a required parameter in the method definition
# The self argument must always come first
# Every method call associated with an instance automatically passes self,
# which is a reference to the instance itself.
# It gives the individual instance access to the attributes
# and methods in the class
# Whenever an instance is created from a class,
# self does not need to be passed as it passed automatically.
# Instead all other arguments will be passed

# Any variable prefixed with self is available to every method in the class
# These same variables can be accesss through any instance created from the class
"""self.name = name"""
# Variables that are accessed through instances like this are called attributes

# The methods sit() and roll_over() do not need additional information to run
# Therefore, they are given the parameter of self.

"""sit(self)"""
# As a result, the instances created later will have acces to these methods

# Making an Instance from a Class
# Classes can bee seen as a set of instructions for
# how to make an instance
'''
class Dog:

    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialiize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old.")
'''

# With the naming convention,
# It can be assumed that the capaitalized name, dog, is a class
# and a lowercase name refers to a single instance created from a class

# Accessing Attributes
# To access attributes, use dot notation
""""my_dog.name"""

# Calling Methods
# Make the dog sit and roll over

'''
class Dog:

    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialiize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old.")

my_dog.sit()
my_dog.roll_over()

'''

# To call the method, give the name of the instance (my_dog),
# and the method you want to call, seperated by a dot

# Creating Mulitple Instances
#

'''
class Dog:

    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialiize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"\nYout dog is {your_dog.age} year old")
your_dog.sit()

'''
# =========================================================
# Exercise 9-1
# Restaurant:

'''
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"\nThe restarant, {self. restaurant_name}, serves {self.cuisine_type} food.  ")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")


restaurant_0 = Restaurant('TGF', 'American')

Restaurant.describe_restaurant(restaurant_0)

Restaurant.open_restaurant(restaurant_0)

# Exercise 9-2
# Three Restaurants

restaurant_1 = Restaurant('Chipotle', "Mexican")
Restaurant.describe_restaurant(restaurant_1)

restaurant_2 = Restaurant('Olive Garden', 'Italian')
Restaurant.describe_restaurant(restaurant_2)

restaurant_3 = Restaurant('Panda Express', 'Chinese')
Restaurant.describe_restaurant(restaurant_3)

'''
# ======================================================
# Exercise 9-3
# Users:

'''
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def define_user(self):
        """Summerizes the User's Information"""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"\nAge: {self.age} years old")
        print(f"\nLocation: {self.location}")

    def greet_user(self):
        """Prints a Personalized Greeting to the User"""
        print(f"Hello {self.first_name}!")


user_0 = User('lily', 'white', 32, 'london')
User.define_user(user_0)
User.greet_user(user_0)

user_1 = User('mandy', 'brown', 23, 'paris')
User.define_user(user_1)
User.greet_user(user_1)

user_2 = User('kelly', 'black', 53, 'brazil')
User.define_user(user_2)
User.greet_user(user_2)

'''
# ==================================================

# Working with Classes and Instances
# Modifying an attribute
# The Car Class
'''
class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

'''

# Setting a Default Value for an Attribute
# Adding an attribute that changes over time
#   Setting a Default Value for an Attribute
#

'''
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''
# Modifying Attribute Values
# Attribute values can be changed in three ways:
# change the value directly through the instance

'''
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

'''

# set the value through a method

'''
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    """
    def update_odometer(self, mileage):
        #Set the odometer reading to the given value.
        self.odometer_reading = mileage
    """
    # Extending the method update_odometer() to do additional work
    # every time reading is notified

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
'''

# increment the value through a method

'''
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

'''
# These methods can controll how users update the odometer
# but anyone with access to the program can change it.

# ==========================================================

# Exercise 9-4:
# Number Served:

'''
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(
            f"\nThe restarant, {self. restaurant_name}, serves {self.cuisine_type} food.  ")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, customers_served):
        """Allow user to increment the number of customer served."""
        self.number_served += customers_served


restaurant = Restaurant('TGF', 'American')
restaurant.describe_restaurant()
Restaurant.open_restaurant(restaurant)

print(f"This buisness has served {restaurant.number_served} people!")

restaurant.number_served = 78
print(f"This buisness has served {restaurant.number_served} people!")

restaurant.set_number_served(786)
print(f"This buisness has served {restaurant.number_served} people!")

restaurant.increment_number_served(970)

print(f"This buisness has served {restaurant.number_served} people!")
'''

# Exercise 9-5
# Login Attempts

'''
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def define_user(self):
        """Summerizes the User's Information"""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"\nAge: {self.age} years old")
        print(f"\nLocation: {self.location}")

    def greet_user(self):
        """Prints a Personalized Greeting to the User"""
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User('lily', 'white', 32, 'london')
User.define_user(user_0)
User.greet_user(user_0)

user_1 = User('mandy', 'brown', 23, 'paris')
User.define_user(user_1)
User.greet_user(user_1)

user_2 = User('kelly', 'black', 53, 'brazil')
User.define_user(user_2)
User.greet_user(user_2)

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()

print(f"\n{user_0.first_name} has attempted to login in {user_0.login_attempts} times")

user_0.reset_login_attempts()

print(f"\n{user_0.first_name} has attempted to login in {user_0.login_attempts} times")

'''

# ====================================================

# Inheritance
# If the class you're writtign is a specialized version of another
# class you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes
# and methods of the first class.
# The original class is called the parent
# The new class is called the child

# The __init_() Method for a Child Class
# When writing a new class based on an existing class,
# It is best to call the __init__ method from the parent class.
# This will initialize any attributes that were defined in the
# parent __init__ method and make the availible in the child class
#
# Ex. creating an electric car
# Electic car class (child), will inherit from the Car class (parent)

'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

'''

# The parent class must be apart of the current file and
# must appear before the child class in the file
# When defining a child class, the name of the parent class
# must be included in parentheses
# The __init__ method takes in the information required
# to make a Car instance
# The super() function is a special function that
# that allows you to call a method from the parent class

# Defining Attributes and Methods for the Child Class
# Add a battery size to the list of attributes

'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the batter size."""
        print(f"This car has a {self.battery_size} -kWh battery")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

'''
# The new attribute, battery_size, is included in the ElectricCar class
# but not the Car class
# the method, describe_battery(), prints information about the battery
#
# An attribute or method that can belong to any car
# should be added to the Car class rather than a specific class

# Overriding Methods from the Parent Class

# To do this, define a method in the child class with
# the same name as the method you want to override in the parent class
# Ex. If the class Car had a method called fill_gas tank()
# Method to override it

"""
    class ElectricCar(Car):
        ---snip---

        def fill_gas_tank(self):
            """"Electric cars dont have gas tanks.""""
import car
            print("This care doesn't need a gas tank!")

"""

# If someone tries to call fill_gas tank() withand electic car,
# Python will ignore the method fill_gas_tank() in Car and run
# this code instead

# Instances as Attributes
# When a list of attributes start to become lengthy
# the class can be broken down into smaller classes
# that work together

# Moving battery attribute and methods from Car class to
# its own class called Battery

'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")



class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)\

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
'''

# Adding another method to battery that reports the range
# of the car based on battery size

'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")




class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

'''

# ==============================

# Exercise 9-6
'''

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(
            f"\nThe restarant, {self. restaurant_name}, serves {self.cuisine_type} food. ")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, customers_served):
        """Allow user to increment the number of customer served."""
        self.number_served += customers_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def read_flavors(self):
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


icy_ice_cream = IceCreamStand('Icy Ice cream')
icy_ice_cream.flavors = ['vanilla', 'chocolate', 'strawberry']

icy_ice_cream.describe_restaurant()
icy_ice_cream.read_flavors()
'''
# Execise 9-7
# Admin
#

'''
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def define_user(self):
        """Summerizes the User's Information"""
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"\nAge: {self.age} years old")
        print(f"\nLocation: {self.location}")

    def greet_user(self):
        """Prints a Personalized Greeting to the User"""
        print(f"Hello {self.first_name}!")
'''
# Execise 9-8
# Privileges

'''
class Privileges:
    def __init__(self, privileges):
        self.privileges = []


    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\n This user -{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
    """
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\n This user -{privilege}")
    """


user_2 = Admin('kelly', 'black', 53, 'brazil')

user_2.privileges = ['can add post', 'can delete post',
                     'can ban user', 'can edit post']

user_2.privileges.show_privileges()
'''

# Execise 9-9
# Battery Upgrade

'''


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def update_battery(self):


class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of a parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''

# Imporitng Classes
# Importing a single class

"""
from car import Car
my_new_car = Car('Audi','a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

"""

# Storing Multiple Classes in a Module

"""
from car import ElectricCar
my_telsa = ElectricCar('tesla', 'model s', 2019)

print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()

"""

# Storing Multiple Classes from a Module

'''
from car import Car, ElectricCar

my_bettle = Car('volkswagen', 'bettle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

'''

# Importing an Entire Module

'''
my_bettle = car.Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
'''

# Importing All Classes from a Module
"""from module_name import* """

# Importing a Module into a Module

""" A set of classes that can be used to represent electric cars"""
'''
from car import Car
from electric_car import ElectricCar

my_bettle = Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

'''