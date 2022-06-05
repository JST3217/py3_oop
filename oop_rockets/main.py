from rocket_classes import *

aspera = {
    "name": "ASPERA",
    "mass": 11,
}
vera = {
    "name": "VeRa",
    "mass": 29,
}
spicam = {
    "name": "SPICAM",
    "mass": 73,
}

payload_list = [aspera, vera, spicam]

falcon_1 = {
    "name": "Falcon 1",
    "speed": 255,
}
falcon_9 = {
    "name": "Falcon 9",
    "speed": 348,
}
falcon_heavy = {
    "name": "Falcon Heavy",
    "speed": 282,
}
starship = {
    "name": "Starship",
    "speed": 330,
}
ariane_5 = {
    "name": "Ariane 5",
    "speed": 310,
}
vega = {
    "name": "Vega",
    "speed": 280,
}

launch_vehicle_list = [falcon_1, falcon_9, falcon_heavy, starship, ariane_5, vega]

baikonor = {
    "name": "Baikonur Cosmodrome",
    "longitude": 46,
    "latitude": 63,
}
cape = {
    "name": "Cape Canaveral Space Force Station",
    "longitude": 28,
    "latitude": -81,
}
guiana = {
    "name": "Guiana Space Centre",
    "longitude": 5,
    "latitude": -53,
}

launch_site_list = [baikonor, cape, guiana]

payload = []
for __ in range(len(payload_list)):
    payload.append(Payload(payload_list[__]["name"],
                                          payload_list[__]["mass"]))

launch_vehicle = []
for __ in range(len(launch_vehicle_list)):
    launch_vehicle.append(LaunchVehicle(launch_vehicle_list[__]["name"],
                                                       launch_vehicle_list[__]["speed"]))

launch_site = []
for __ in range(len(launch_site_list)):
    launch_site.append(LaunchSite(launch_site_list[__]["name"],
                                                 launch_site_list[__]["longitude"],
                                                 launch_site_list[__]["latitude"]))

NUMBER_OF_ROCKETS = 4

launch_1 = RocketFleet(NUMBER_OF_ROCKETS, launch_vehicle, payload)
print(launch_1)
for __ in range(len(launch_1)):
    chosen_launch_site = random.choice(launch_site)
    chosen_launch_angle = random.randrange(-90, 90 + 1, 5)
    print(f'launching...\n'
          f'  LV: {launch_1[__].launch_vehicle.name}\n'
          f'  PL: {launch_1[__].payload.name}\n'
          f'  LS: {chosen_launch_site.name} [{chosen_launch_site.longitude},{chosen_launch_site.latitude}]\n'
          f'  LA: {chosen_launch_angle}deg')
    launch_1[__].launch(chosen_launch_site, chosen_launch_angle)

# s = RocketFleet.get_distance(launch_1[0], launch_1[1])
# print(round(s, 2))
# print(launch_1.number_of_rockets())
# print(Rocket.next_id)
