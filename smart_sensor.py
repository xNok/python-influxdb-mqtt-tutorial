"""
MQTT Smart temperature Sensor
"""

import time

import paho.mqtt.client as mqtt
from faker import Faker

# let's connect to the MQTT broker
MQTT_BROKER_URL    = "mqtt.eclipseprojects.io"
MQTT_PUBLISH_TOPIC = "temperature"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)

# Init faker our fake data provider
fake = Faker()

# Infinit loop of fake data sent to the Broker
while True:
    temperature = fake.random_int(min=0, max=30)
    mqttc.publish(MQTT_PUBLISH_TOPIC, temperature)
    print(f"Published new temperature measurement: {temperature}")
    time.sleep(1)
