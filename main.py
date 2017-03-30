from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import machine
import time
import network


# Default MQTT server to connect to
SERVER = "m11.cloudmqtt.com"
PORT = 15034
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"hello/world"

USER = "oyqmvonl"
PASSWORD = "eCPIJkxVFWBU"


led = Pin(5, Pin.OUT, value=1)


def do_connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('XT1580 7008', '80a34ac3c19c')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b"0":
        led.value(0)
    elif msg == b"1":
        led.value(1)


def main():

    do_connect_wifi()
    
    c = MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSWORD)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect(clean_session=False)
    c.subscribe(TOPIC,qos=1)
    print("Connected to %s, subscribed to %s topic" % (SERVER, TOPIC))

    try:
        while 1:
            
            if not network.WLAN(network.STA_IF).isconnected():
                do_connect_wifi()
            
            try:
                print('check mensage...')
                c.check_msg()
            except:
                print('error on check mensage...')
                while 1:
                    try:
                        print('try reconnect...')
                        c.connect(False)
                        break
                    except:
                        print('error on reconnect...')
                    
                    time.sleep(2)
                    

            time.sleep(2)
    finally:
        c.disconnect()
        
if __name__ == "__main__":
    main()
