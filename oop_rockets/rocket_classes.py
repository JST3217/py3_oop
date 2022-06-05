from __future__ import annotations
import math
import random
from math import sqrt, sin, cos


class Payload:
    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass

    def __str__(self):
        return f'Payload obj \n' \
               f'name: {self.name} \n' \
               f'  mass: {self.mass}kg \n'


class LaunchVehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f'LaunchVehicle obj \n' \
               f'name: {self.name} \n' \
               f'  speed: {self.speed} \n'


class LaunchSite:
    def __init__(self, name: str, longitude: float, latitude: float):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f'LaunchSite obj \n' \
               f'name: {self.name} \n' \
               f'  coordinates: [{self.longitude},{self.latitude}] \n'


class Rocket:
    next_id = 1

    def __init__(self, obj_1: LaunchVehicle, obj_2: Payload):
        self.launch_vehicle = obj_1
        self.payload = obj_2
        self.alt = 0
        self.long = 0
        self.lat = 0
        self.id = Rocket.next_id
        Rocket.next_id += 1

    def launch(self, obj_1: LaunchSite, launch_angle: int):
        self.long = obj_1.longitude
        self.lat = obj_1.latitude
        launch_angle_rad = math.radians(launch_angle)
        x = cos(launch_angle_rad)
        y = sin(launch_angle_rad)
        if random.random() > (5.8 / 100):  # 5.8% launch failure rate,
            # source:https://blogs.scientificamerican.com/life-unbounded/rocket-launches-are-surprisingly-successful/
            print("rocket takeoff")
            for __ in range(10):
                self.alt += self.launch_vehicle.speed * 10 / self.payload.mass
                self.long += y * 10
                self.lat += x * 10
            print("final alt:", round(self.alt, 2))
        else:
            print("launch failed")

    def get_distance_from_launch_site(self, obj: LaunchSite) -> float:
        x_1 = obj.latitude
        y_1 = obj.longitude
        z_1 = 0

        x_2 = self.lat
        y_2 = self.long
        z_2 = self.alt

        return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_2 - z_1) ** 2)

    def __str__(self):
        return f'Rocket obj \n' \
               f'LV: {self.launch_vehicle.name} \n' \
               f'PL: {self.payload.name} \n' \
               f'altitude: {self.alt} \n'


class RocketFleet:
    def __init__(self, amount_of_rockets: int, rocket_list: list, payload_list: list):
        self.rocket_fleet = []
        for __ in range(amount_of_rockets):
            chosen_rocket = random.choice(rocket_list)
            chosen_payload = random.choice(payload_list)
            self.rocket_fleet.append(Rocket(chosen_rocket, chosen_payload))

    def __str__(self):
        string = "RocketFleet obj \n" \
                 "[LV] - [PL] for this launch:\n"
        for __ in self.rocket_fleet:
            string += f'{__.launch_vehicle.name} - {__.payload.name} \n'
        return string

    def __getitem__(self, key):
        return self.rocket_fleet[key]

    def __len__(self):
        return self.number_of_rockets()

    def number_of_rockets(self):
        return len(self.rocket_fleet)

    @staticmethod
    def get_distance(obj1: Rocket, obj2: Rocket) -> float:
        x_1 = obj1.lat
        y_1 = obj1.long
        z_1 = obj1.alt

        x_2 = obj2.lat
        y_2 = obj2.long
        z_2 = obj2.alt

        return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_2 - z_1) ** 2)
