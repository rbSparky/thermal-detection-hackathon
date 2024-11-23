from machine import I2C, Pin
import time
import network
import ubinascii
from umqtt.simple import MQTTClient
import ssd1306

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# MQTT Broker details
MQTT_BROKER = "test.mosquitto.org"  # Replace with your ngrok public address
MQTT_PORT = 1883              # Replace with your ngrok port
MQTT_TOPIC = "testicals/topic"       # Topic to subscribe to

# Wi-Fi credentials
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# Initialize the buzzer and LED
buzzer = Pin(27, Pin.OUT)
led = Pin(23, Pin.OUT)

# Function to connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# Function to handle received MQTT messages
def message_callback(topic, msg):
    print("Received message:", msg)
    if msg == b"on":  # Turn on buzzer and LED
        buzzer.on()
        led.on()
        oled.text('Animal Detected!', 10, 10)      
        oled.text('Drive Slow!!!!', 10, 18)
        oled.show()
        print("Buzzer and LED turned ON")
    elif msg == b"off":  # Turn off buzzer and LED
        buzzer.off()
        led.off()
        oled.fill(0);      
        oled.show()
        print("Buzzer and LED turned OFF")

# Connect to MQTT Broker and Subscribe
def connect_to_mqtt():
    client_id = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    print(network.WLAN().config('mac'))
    print("client id: ", client_id)
    client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT)
    client.set_callback(message_callback)
    client.connect()
    print("Connected to MQTT Broker")
    client.subscribe(MQTT_TOPIC)
    print(f"Subscribed to topic: {MQTT_TOPIC}")
    return client

# Main program
try:
    connect_to_wifi()
    mqtt_client = connect_to_mqtt()

    while True:
        # Wait for messages from the broker
        mqtt_client.check_msg()
        time.sleep(0.1)

except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Cleaning up...")
    buzzer.off()
    led.off()
