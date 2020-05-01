from message_eater.mongo import Mongo
from message_eater.mqtt import MQTT
from signal import pause

mongo = Mongo()
mqtt = MQTT(mongo)

mongo.connect()
mqtt.run()

try:
    pause()
except KeyboardInterrupt:
    pass

mqtt.stop()
mongo.disconnect()
