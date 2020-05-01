# Publisher
import paho.mqtt.client as mqtt
import sys

# Vars
#MQTT_BROKER = "localhost"
MQTT_BROKER = "mosquitto" # Docker version
MQTT_PORT = 1883

# Basic Configuration
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

# Check arguments
if len(sys.argv) == 2:
    topic = sys.argv[1]
else:
    topic = "testing/test"


# Main
while True:
    client.publish(topic, input('Message : '))
