# This file is executed on every boot (including wake-boot from deepsleep)

# import uos

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

time.sleep(3)

    # esp.osdebug(None)
    # gc.collect()
# uos.dupterm(None, 1) # disable REPL on UART(0)
# import webrepl
# webrepl.start()

ssid = 'young-family'
password = 'good2best'
mqtt_server = '192.168.31.133'
# EXAMPLE IP ADDRESS
# mqtt_server = '192.168.1.144'

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'#'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() is False:
    pass

print('Connection successful')
print(station.ifconfig())