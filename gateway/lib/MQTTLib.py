import MQTTConst as mqttConst
import MQTTClient as mqttClient

class AWSIoTMQTTClient:

    def __init__(self, clientID, protocolType=mqttConst.MQTTv3_1_1, useWebsocket=False, cleanSession=True):
        self._mqttClient = mqttClient.MQTTClient(clientID, cleanSession, protocolType)

    # Configuration APIs
    def configureLastWill(self, topic, payload, QoS):
        self._mqttClient.setLastWill(topic, payload, QoS)

    def clearLastWill(self):
        self._mqttClient.clearLastWill()

    def configureEndpoint(self, hostName, portNumber):
        self._mqttClient.configEndpoint(hostName, portNumber)

    def configureIAMCredentials(self, AWSAccessKeyID, AWSSecretAccessKey, AWSSessionToken=""):
        self._mqttClient.configIAMCredentials(AWSAccessKeyID, AWSSecretAccessKey, AWSSessionToken)

    def configureCredentials(self, CAFilePath, KeyPath="", CertificatePath=""):  # Should be good for MutualAuth certs config and Websocket rootCA config
        self._mqttClient.configCredentials(CAFilePath, KeyPath, CertificatePath)

    def configureAutoReconnectBackoffTime(self, baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond):
        self._mqttClient.setBackoffTiming(baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond)

    def configureOfflinePublishQueueing(self, queueSize, dropBehavior=mqttConst.DROP_NEWEST):
        self._mqttClient.setOfflinePublishQueueing(queueSize, dropBehavior)

    def configureDrainingFrequency(self, frequencyInHz):
        self._mqttClient.setDrainingIntervalSecond(1/float(frequencyInHz))

    def configureConnectDisconnectTimeout(self, timeoutSecond):
        self._mqttClient.setConnectDisconnectTimeoutSecond(timeoutSecond)

    def configureMQTTOperationTimeout(self, timeoutSecond):
        self._mqttClient.setMQTTOperationTimeoutSecond(timeoutSecond)

    # MQTT functionality APIs
    def connect(self, keepAliveIntervalSecond=30):
        return self._mqttClient.connect(keepAliveIntervalSecond)

    def disconnect(self):
        return self._mqttClient.disconnect()

    def publish(self, topic, payload, QoS):
        return self._mqttClient.publish(topic, payload, QoS, False)  # Disable retain for publish by now

    def subscribe(self, topic, QoS, callback):
        return self._mqttClient.subscribe(topic, QoS, callback)

    def unsubscribe(self, topic):
        return self._mqttClient.unsubscribe(topic)


