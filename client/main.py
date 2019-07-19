# import LM75A
import time
from machine import Pin

def sub_cb(topic, msg):
    door_open = Pin(12, Pin.OUT)
    handset = Pin(13, Pin.OUT)
    statusled = Pin(2, Pin.OUT)
    top = b'open'
    mes = b'0'
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
        print('ESP received hello message')
        statusled.value(0)
    elif topic == b'notification' and msg == b'0':
        statusled.value(1)
    elif topic == b'door_open' and msg == b'0':
        door_open.value(0)
    elif topic == b'door_open' and msg == b'1':
        door_open.value(1)
    elif topic == b'handset' and msg == b'0':
        handset.value(0)
    elif topic == b'handset' and msg == b'1':
        handset.value(1)
    elif topic == b'open' and msg == b'1':
        handset.value(1)
        time.sleep_ms(500)
        door_open.value(1)
        time.sleep(3)
        door_open.value(0)
        time.sleep_ms(500)
        handset.value(0)
        client.publish(top, mes)

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

while True:
#     try:
#         temp = LM75A.getTemp(72)
#     except:
#         temp = -100500

    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
            # msg = 'Hello #{0} with temp {1}'.format(counter, LM75A.getTemp())
            # msg = b'Hello #%d' % counter
            # msg = b'The temp is %dC' % temp
            msg = b'Ping'
            client.publish(topic_pub, msg)
            last_message = time.time()
            # counter += 1
    except OSError as e:
        restart_and_reconnect()