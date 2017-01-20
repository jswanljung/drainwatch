import machine
from network import WLAN


if machine.reset_cause() != machine.SOFT_RESET:
    wlan = WLAN(mode=WLAN.STA)
    #wlan.ifconfig(config=('192.168.1.201',  '255.255.255.0',  '192.168.1.1', '213.80.98.2'))
    nets = wlan.scan()
    for net in nets:
        if net.ssid=='S-FW Net':
            wlan.connect(ssid=net.ssid,  auth=(net.sec,  'glutamathimmel'))
            while not wlan.isconnected():
               machine.idle()
            break

#from machine import UART
#import os
#uart = UART(0, 115200)
#os.dupterm(uart)

