# Publisher
import paho.mqtt.client as mqtt
import sys

# Vars
#MQTT_BROKER = "mosquitto" # Docker version
#MQTT_PORT = 1883
MQTT_BROKER = "158.49.113.46"   # IP Máquina demo
MQTT_PORT = 80                  # Puerto 80 para demo.

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
