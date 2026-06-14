import json
import paho.mqtt.client as mqtt

BROKER = "localhost"

TOPIC = "home/energy"

client = mqtt.Client()

client.connect(BROKER,1883)

def publish_sensor_data(data):

    payload = json.dumps(data)

    client.publish(
        TOPIC,
        payload
    )