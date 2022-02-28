"""
MQTT subscriber - Listen to a topic and sends data to InfluxDB
"""

import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point
import paho.mqtt.client as mqtt
import struct


load_dotenv()  # take environment variables from .env.

# InfluxDB config
BUCKET = os.getenv('INFLUXDB_BUCKET')
client = InfluxDBClient(url=os.getenv('INFLUXDB_URL'),
                token=os.getenv('INFLUXDB_TOKEN'), org=os.getenv('INFLUXDB_ORG'))
write_api = client.write_api()

# MQTT broker config
MQTT_BROKER_URL    = "mqtt.eclipseprojects.io"
MQTT_PUBLISH_TOPIC = "temperature"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)

def on_connect(client, userdata, flags, rc):
    """ The callback for when the client connectes to the broker."""
    print("Connected with result code "+str(rc))

    # Subscribe tp a topic
    client.subscribe(MQTT_PUBLISH_TOPIC)

def on_message(client, userdata, msg):
    """ The callback for when a PUBLISH message is received from the server."""
    print(msg.topic+" "+str(msg.payload))

    # We recived bytes we need to converts into something usable
    measurement = int(msg.payload)

    ## InfluxDB logic
    point = Point(MQTT_PUBLISH_TOPIC).tag("location", "New York").field("temperature", measurement )
    write_api.write(bucket=BUCKET, record=point)


## MQTT logic - Register callbacks and start MQTT client
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.loop_forever()
