import paho.mqtt.client as paho

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
    client.subscribe("notice", qos=2)

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.username_pw_set("subscriber", "subscriber@1234!")

client.connect("localhost", 1883)


client.loop_forever()
