from rocket_classes import *


NUMBER_OF_ROCKETS = 4
RANDOM_SEED = 98

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


def setup():
    """
    The setup function creates a list of payloads, launch vehicles, and launch sites.
    The lists are then returned to the main function.

    return: a list of payload, launch vehicle and launch site as objects
    """
    payload_list = [aspera, vera, spicam]
    launch_vehicle_list = [falcon_1, falcon_9, falcon_heavy, starship, ariane_5, vega]
    launch_site_list = [baikonor, cape, guiana]

    payload = []
    for _, __ in enumerate(payload_list):
        payload.append(Payload(__.get('name'), __.get('mass')))

    launch_vehicle = []
    for _, __ in enumerate(launch_vehicle_list):
        launch_vehicle.append(LaunchVehicle(__.get('name'), __.get('speed')))

    launch_site = []
    for _, __ in enumerate(launch_site_list):
        launch_site.append(LaunchSite(__.get('name'), __.get('longitude'), __.get('latitude')))

    return payload, launch_vehicle, launch_site


def run():
    """
    The run function launches a fleet of rockets.

    The run function launches a fleet of rockets, each with its own payload and launch vehicle.
    The number of rockets to be launched is specified by the user.
    Each rocket has an independent probability to choose a random launch site from our database.

    return: The rocket fleet
    """
    launch = RocketFleet(NUMBER_OF_ROCKETS, launch_vehicle, payload)
    print(launch)
    for _, __ in enumerate(launch):
        chosen_launch_site = random.choice(launch_site)
        chosen_launch_angle = random.randrange(-90, 90 + 1, 5)
        print(f'launching...\n'
              f'  LV: {__.launch_vehicle.name}\n'
              f'  PL: {__.payload.name}\n'
              f'  LS: {chosen_launch_site.name} [{chosen_launch_site.longitude},{chosen_launch_site.latitude}]\n'
              f'  LA: {chosen_launch_angle}deg')

        # Launch!
        __.launch(chosen_launch_site, chosen_launch_angle)

    return launch


# Setup and start the simulation
print("Simple rocket simulation")
random.seed(RANDOM_SEED)  # This helps to reproduce results

# Start the setup process
payload, launch_vehicle, launch_site = setup()

# Launch!
launch_01 = run()
