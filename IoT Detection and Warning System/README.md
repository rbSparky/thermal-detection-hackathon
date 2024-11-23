A system that detects stray animals in low-lighting environments using thermal sensors near highways/roads and sends an alert signal to an edge IOT device, equipped with LEDs and ultrasonic sound emitters, using MQTT Protocol to deter the animals from coming too close.

# MQTT Communication protocol
MQTT (Message Queuing Telemetry Transport) is a lightweight IoT communication protocol designed for low-powered devices and reliable communication over unreliable networks. It employs a "publish/subscribe" (pub/sub) messaging architecture, involving three main participants:
<img src="https://camo.githubusercontent.com/0d7b840195f1be43abc6f28720224dde9b6bfa0a0a9ce73648d16a76b6154ce3/68747470733a2f2f6d7174742e6f72672f6173736574732f696d672f6d7174742d7075626c6973682d7375627363726962652e706e67" alt="MQTT demonstration image">
- MQTT Subscriber: A device that subscribes to a specific MQTT topic to receive messages.
- MQTT Publisher: A device that publishes messages to a specific MQTT topic to communicate with clients.
- MQTT Broker: A server that manages communication, propagating messages between publishers and subscribers. One of MQTT's key features is its ability to queue messages in case a subscriber is offline. This ensures no data is lost and previously missed messages are available when the subscriber reconnects.

For the application of this project, we are using a publicly available MQTT Broker, by Eclipse Mosquitto. The MQTT Broker is available at "test.mosquitto.org" and port 1883 allows for free communication. Ports can be configured for encryption and authentication as per the need, or a locally hosted MQTT Broker can also be used.

# IoT Alert System
The device consists of three components: 
- a flashing LED that can be installed roadside for alerting both animals and drivers.
- an ultrasonic sound emitter that emits noise for disturbing animals while drivers stay unaffected.
- an OLED Display Board that can be used for signalling drivers about areas prone to animal presence, or a certain animal's detection.

The device is simulated at Wokwi platform for prototyping purposes.

## ESP32 Board
The ESP32 Board is a popular WiFi and Bluetooth-enabled microcontroller, which serves as the main controlling unit of this device. It controls activation/deactivation for all actuators used and is also responsible for subscribing as a client to the MQTT Broker.

## LED Unit
The LED buld is used as an actuator to provide flashing lights in order to confuse and deter animals while alerting drivers of potential animal in their vicinity.

## Sound Emitter Unit
The Sound Emitter Unit, is responsible for producing ultrasonic sounds at 30-40 kHz, well above the hearing range of human drivers but audible to dogs and cows, which ensures minimal disturbance to drivers.

## OLED Display Unit
The OLED display unit is used as a visual actuator, which can be installed across the highways to display messages to drivers, ensuring there are more than one signals and reducing chances of missing alerts. The OLED display unit is interfaced with the microcontroller using "ssd1306" library which provides functions for controlling the display. 

