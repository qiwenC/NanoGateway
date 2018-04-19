import socket
import struct
import time
from network import LoRa
from network import WLAN
from mqtt import MQTTClient

# A basic package header, B: 1 byte for the deviceId, B: 1 byte for the pkg size, %ds: Formated string for string
_LORA_PKG_FORMAT = "!BB%ds"
# A basic ack package, B: 1 byte for the deviceId, B: 1 bytes for the pkg size, B: 1 byte for the Ok (200) or error messages
_LORA_PKG_ACK_FORMAT = "BBB"

# Setup wlan network
wlan = WLAN(mode=WLAN.STA)
wlan.connect("dragino-1816d9",auth=(WLAN.WPA2,"dragino-dragino"),timeout = 5000)
while not wlan.isconnected():
    time.sleep_ms(50)
print("connected")

#set up the mqtt client and server
client = MQTTClient(client_id ="example_client",server ="io.adafruit.com",user=
                    "Beehive_",password = "ec221d45da514be29cdd5e4cd025f36c",port =1883)
client.connect()

# Open a LoRa Socket, use rx_iq to avoid listening to our own messages

lora = LoRa(mode=LoRa.LORA, rx_iq=True)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)


while (True):
    recv_pkg = lora_sock.recv(512)
    if (len(recv_pkg) > 2):
        recv_pkg_len = recv_pkg[1]
        device_id, pkg_len, mesg = struct.unpack(_LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)
        # If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
        print('Device: %d - Pkg:  %s' % (device_id, mesg))

        ack_pkg = struct.pack(_LORA_PKG_ACK_FORMAT, device_id, 1, 200)
        lora_sock.send(ack_pkg)

        client.publish(topic = "Beehive_/feeds/LoRa",msg = mesg)


