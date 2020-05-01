# Subscriber
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
if len(sys.argv) == 1:
    topics = ["testing/test"]
else:
    topics = sys.argv


# Operations
def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    for t in topics[1:]:
        client.subscribe(t)
        print("Suscribed to: " + t)


def on_message(client, userdata, message):
    print(message.topic + " --> " + message.payload.decode())


# Main
while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
