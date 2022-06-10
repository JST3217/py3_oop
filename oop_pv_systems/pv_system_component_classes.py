import random
from friendly_name_classes import FriendlyName

#python runtime
#python try

# Power production from a solar panel is calculated based on
# (1) the panel’s rated power,
# (2) the solar energy availability (monthly average), and
# (3) efficiency loss due to elevated operating temperatures.

# Power production decreases by 5% for every 10degC increase over the design temperature (25degC).


class SolarPanel:
    def __init__(self):
        self.type = ""
        self.capacity = 300  # Watts
        self.cost = 1


class Battery:
    def __init__(self):
        self.friendly_name = FriendlyName()
        self.type = "Lithium-ion"
        self.lifecycle = 1000
        self.maximum_capacity = 69.12 * 1000
        self.current_capacity = self.maximum_capacity/2

    def __str__(self):
        return f'{self.friendly_name}, {self.type} battery'
