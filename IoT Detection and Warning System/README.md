# animal-detection-and-warning-system
This is a simple IoT-based system animal detection and warning system using an ESP32, a buzzer, an LED, and an OLED display. It leverages the MQTT protocol to communicate with a remote MQTT broker, receiving commands to alert drivers of animal detection events.

For the implementation, we are using a publicly available MQTT Broker, by "Eclipse Mosquitto". The MQTT Broker is available at `"test.mosquitto.org"` and port `1883` allows for free communication. Ports can be configured for encryption and authentication as per the need, or a locally hosted MQTT Broker can also be used.

# Features
- Detects "on" and "off" commands from an MQTT broker.
- Activates an LED and buzzer when an animal is detected.
- Displays warning messages on an OLED display.
- Communicates over Wi-Fi and subscribes to a specific MQTT topic.
- Lightweight and real-time system using the MQTT protocol.

# Components required
- ESP32 microcontroller
- Ultrasonic sound emitter / buzzer (for demonstration purposes)
- LED with a 220Ω resistor
- 0.96-inch OLED display (I2C)
- Connecting wires

# Software required
- [Wokwi Simulator](https://wokwi.com/)
- microPython libraries
  - `umqtt.simple`
  - `ssd1306`
- Public MQTT Broker: `test.mosquitto.org` is a publicly available Eclipse Mosquitto MQTT server/broker. For more information you may [click here](https://test.mosquitto.org/)  

# Circuit Diagram
<img src="https://github.com/quick-fox-03/animal-detection-and-warning-system/blob/main/soundplay%20circuit.jpg?raw=true" height="500px" width="700px" alt="image of circuit with esp32 controller leds and speakers">
Pin connections:

| Component  | ESP32 Pin |
| ------------- | ------------- |
| Sound Emitter  | GPIO 27  |
| LED Bulb  | GPIO 23  |
| OLED (SDA)  | GPIO 21  |
| OLED (SCL)  | GPIO 22  |

[Simulation Link](https://wokwi.com/projects/415272090827317249)

# System Workflow
1. The ESP32 connects to a Wi-Fi network.
2. It subscribes to the MQTT broker at `"test.mosquitto.org"` on port `1883` and listens for messages on the topic testicals/topic.
3. When a message is received:
   - If the message is "on":
     - The LED and buzzer are turned ON.
     - The OLED displays:
     - ```
       Animal Detected!
       Drive Slow!!!!
       ```
   - If the message is "off":
     - The LED and buzzer are turned OFF.
     - The OLED screen is cleared.

# Behaviour on MQTT messages
| Message  | Behaviour |
| ------------- | ------------- |
| `"on"` | Activates the LED and buzzer. Displays warnings on the OLED.  |
| `"off"`  | Deactivates the LED and buzzer. Clears the OLED screen. |

# Setup instructions
1. Hardware setup: Connect the components as per the circuit diagram.
2. Wi-Fi configuration: Replace `WIFI_SSID` and `WIFI_PASSWORD` in the code with your Wi-Fi credentials. Wokwi's platform simulates a Wi-Fi network, for using it add the following credentials:
   - `WIFI_SSID` : "Wokwi-GUEST"
   - `WIFI_PASSWORD`: ""
3. MQTT Broker: Use a public MQTT broker [Mosquitto](https://test.mosquitto.org/) or configure your private broker.
4. Upload Code: Use a suitable IDE (such as Arduino IDE) to upload the code to the ESP32.
5. Testing: Publish `on` or `off` messages to the topic `"save-the-stray/INDCYC"` on the broker to test the system.

 # Code Explanation
 ## Wi-Fi Connection
 The `connect_to_wifi()` function establishes a Wi-Fi connection using the provided SSID and password.
## MQTT Connection
The `connect_to_mqtt()` function connects to the MQTT broker and subscribes to the topic `"save-the-stray/INDCYC"`. A unique client ID is generated based on the ESP32’s MAC address.
## Message Handling
The `message_callback()` function processes incoming MQTT messages:
- If `msg == b"on"`, it activates the LED and buzzer and displays warnings on the OLED.
- If `msg == b"off"`, it deactivates the LED and buzzer and clears the OLED.

# Testing the system
1. Publish Test Messages: Use an MQTT client (For e.g. Eclipse Mosquitto or a Python script) to publish messages on the topic `"save-the-stray/INDCYC"`.
2. Observe the behaviour:
   - For `"on"` The LED and buzzer should turn on, and the OLED should display the warning.
   - For `"off"` The LED and buzzer should turn off, and the OLED should clear.

# Live simulation of circuit
Check out the circuit at [Wokwi here](https://wokwi.com/projects/415272090827317249)

# Learn about the MQTT Communication protocol
MQTT (Message Queuing Telemetry Transport) is a lightweight IoT communication protocol designed for low-powered devices and reliable communication over unreliable networks. It employs a "publish/subscribe" (pub/sub) messaging architecture for providing minimal overhead. [Learn more about MQTT here. ](https://mqtt.org/)

