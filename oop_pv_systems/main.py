from pv_system_component_classes import *
import simpy


env = simpy.Environment()

x = [Battery() for _ in range(2)]

for count, __ in enumerate(x):
    print(__)
