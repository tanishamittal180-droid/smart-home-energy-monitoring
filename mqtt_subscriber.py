import json

import paho.mqtt.client as mqtt

from simulation.database import insert_energy

BROKER = "localhost"

TOPIC = "home/energy"


def on_message(client,userdata,msg):

    payload = json.loads(
        msg.payload.decode()
    )

    insert_energy(payload)

    print(
        "Stored:",
        payload["appliance"]
    )


client = mqtt.Client()

client.on_message = on_message

client.connect(
    BROKER,
    1883
)

client.subscribe(
    TOPIC
)

client.loop_forever()