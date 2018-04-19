# wifi configuration
WIFI_SSID = 'YOUR_WIFI_NAME'
WIFI_PASS = 'PASSWORD'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'YOUR_AWS_HOST'
AWS_ROOT_CA = '/flash/cert/root-CA.crt'
AWS_CLIENT_CERT = '/flash/cert/certificat"
AWS_PRIVATE_KEY = '/flash/cert/privatekey'
################## Subscribe / Publish client #################
CLIENT_ID = 'LoPy'
TOPIC = 'LoPy'
DEVICE_TOPIC = 'myTestTopic/deviceID'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'PublishTopic' #？
LAST_WILL_MSG = 'To All: Last will message'#？

# A basic package header, B: 1 byte for the deviceId, B: 1 byte for the pkg size, %ds: Formated string for string
_LORA_PKG_FORMAT = "!BB%ds"
# A basic ack package, B: 1 byte for the deviceId, B: 1 bytes for the pkg size, B: 1 byte for the Ok (200) or error messages
_LORA_PKG_ACK_FORMAT = "BBB"
