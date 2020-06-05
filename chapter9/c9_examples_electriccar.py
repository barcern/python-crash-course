# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:57:38 2020

@author: barbora

A set of classes that can be used to represent electric cars.

"""

# Import Car class
from c9_examples_gascar import CarModule

class BatteryModule:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCarModule(CarModule):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = BatteryModule()
