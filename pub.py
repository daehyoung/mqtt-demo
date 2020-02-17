import paho.mqtt.publish as publish
from datetime import datetime

msg = "hello :" + str(datetime.now())
publish.single(topic="notice", payload=msg, hostname="localhost",port = 1883, auth = { 'username' : 'publisher', 'password' : 'publisher@1234!' })
