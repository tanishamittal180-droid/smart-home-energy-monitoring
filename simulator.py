import random

from datetime import datetime

from simulation.appliance_manager import (
    get_appliances
)

VOLTAGE = 230

TARIFF = 8

CARBON = 0.82

def generate_sensor_data():

    appliance = random.choice(
        get_appliances()
    )

    name = appliance[0]

    room = appliance[1]

    rated_power = appliance[2]

    status = appliance[3]

    if status == "ON":

        power = rated_power * random.uniform(
            0.8,
            1.2
        )

    else:

        power = 0

    current = power / VOLTAGE

    energy = power/1000/60

    cost = energy*TARIFF

    carbon = energy*CARBON

    alert = "NORMAL"

    if power > 1500:

        alert = "HIGH ENERGY"

    return {

        "timestamp":str(
            datetime.now()
        ),

        "room":room,

        "appliance":name,

        "status":status,

        "voltage":VOLTAGE,

        "current":round(
            current,2
        ),

        "power":round(
            power,2
        ),

        "energy":round(
            energy,4
        ),

        "cost":round(
            cost,2
        ),

        "carbon":round(
            carbon,3
        ),

        "alert":alert
    }