from friendly_name_classes import FriendlyName


class Battery:
    def __init__(self):
        self.friendly_name = FriendlyName()
        self.type = "Lithium-ion"
        self.lifecycle = 1000
        self.maximum_capacity = 69.12 * 1000
        self.current_capacity = self.maximum_capacity/2

    def __str__(self):
        return f'{self.friendly_name}, {self.type} battery'


class SolarPanel:
    def __init__(self):
        self.type = ""
        self.capacity = 300  # Watts
        self.cost = 1
