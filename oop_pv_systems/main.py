# from pv_system_component_classes import *
from friendly_name_classes import FriendlyName
import simpy
import random


class G:
    RANDOM_SEED = 98
    NUM_CHARGERS = 2          # Number of battery chargers
    CHARGETIME = 2.304*60     # Minutes it takes to charge a battery
    T_INTER = 60*2            # Create a battery every ~60 minutes
    NUM_BATTERIES_INIT = 4    # Number of batteries at the start of simulation
    SIM_TIME = 9*60           # Simulation time in minutes
    NUM_RUNS = 2              # Number of simulations


class Battery:
    def __init__(self, battery_id: int):
        # self.friendly_name = FriendlyName()
        self.id = battery_id
        self.status = "Empty"  # Charging, Discharging, Idle
        self.current_capacity_percentage: int = 0
        # self.current_lifecycle = 0


class BatterySwappingModel:
    def __init__(self):
        self.env = simpy.Environment()
        self.battery_counter = 0

        self.charger = simpy.Resource(self.env, capacity=G.NUM_CHARGERS)

    def battery_generator(self):
        if self.battery_counter == 0:
            for __ in range(G.NUM_BATTERIES_INIT):
                self.battery_counter += 1
                battery = Battery(self.battery_counter)
                self.env.process(self.charging(battery))

        while True:
            self.battery_counter += 1

            battery = Battery(self.battery_counter)

            self.env.process(self.charging(battery))

            sampled_interarrival = random.expovariate(1.0 / G.T_INTER)

            yield self.env.timeout(sampled_interarrival)

    def charging(self, battery):
        if battery.current_capacity_percentage != 100:
            print(f'Battery {battery.id} started queueing at {round(self.env.now)}')

            with self.charger.request() as req:
                yield req

                print(f'Battery {battery.id} started charging at {round(self.env.now)}')
                yield self.env.timeout(G.CHARGETIME)
                print(f'Battery {battery.id} finished charging at {round(self.env.now)}')

    def run(self):
        self.env.process(self.battery_generator())

        self.env.run(until=G.SIM_TIME)


for run in range(G.NUM_RUNS):
    # random.seed(G.RANDOM_SEED)
    print(f'Run {run+1} of {G.NUM_RUNS}')
    my_battery_swapping_model = BatterySwappingModel()
    my_battery_swapping_model.run()
    print()  # newline between runs
