import os
import socket
import time
import utime
import struct
import machine
import binascii
import json
import gc
from network import LoRa
from machine import RTC

# A basic package header, B: 1 byte for the deviceId, B: 1 bytes for the pkg size
_LORA_PKG_FORMAT = "BB%ds"
_LORA_PKG_ACK_FORMAT = "BBB"
DEVICE_ID = 0x01

rtc = machine.RTC()
rtc.ntp_sync("uk.pool.ntp.org")
utime.sleep_ms(750)
print(rtc.now())

gc.enable

# get MAC address as the device ID
deviceID = binascii.hexlify(machine.unique_id())

# Open a Lora Socket, use tx_iq to avoid listening to our own messages
lora = LoRa(mode=LoRa.LORA, tx_iq=True)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)

count = 1
while(True):
    # Package send containing a simple string
    message = {}
    message['deviceID'] = deviceID
    timestamp = utime.localtime()
    message['timestamp'] = "%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0],timestamp[1],timestamp[2],timestamp[3],timestamp[4],timestamp[5])
    message['count'] = count
    msg = json.dumps(message)
    pkg = struct.pack(_LORA_PKG_FORMAT % len(msg), DEVICE_ID, len(msg), msg)
    lora_sock.send(pkg)
    print(msg)
    count = count + 1
    # Wait for the response from the gateway. NOTE: For this demo the device does an infinite loop for while waiting the response. Introduce a max_time_waiting for you application
    waiting_ack = True
    while(waiting_ack):
        recv_ack = lora_sock.recv(256)

        if (len(recv_ack) > 0):
            device_id, pkg_len, ack = struct.unpack(_LORA_PKG_ACK_FORMAT, recv_ack)
            if (device_id == DEVICE_ID):
                if (ack == 200):
                    waiting_ack = False
                    # If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
                    print("ACK")
                else:
                    waiting_ack = False
                    # If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
                    print("Message Failed")


    time.sleep(20)
