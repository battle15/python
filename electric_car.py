
""" A set of classes that can be used to represent electric cars"""

from car import Car

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

