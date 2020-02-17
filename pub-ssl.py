import paho.mqtt.publish as publish
from datetime import datetime
import ssl

certs = '/home/daehyoung/mqtt/certs/ca.crt'

tls = { 'ca_certs': certs }
msg = "hello :" + str(datetime.now())

publish.single(topic = "notice", payload= msg, hostname= "localhost", port = 8883, auth = { 'username' : 'publisher', 'password' : 'publisher@1234!' },tls=tls)
