## Video demonstration 



https://github.com/user-attachments/assets/f8fb8a0e-9366-40ab-acf8-3f7320ebafb2



## Architecture Diagram

![](https://github.com/rbSparky/thermal-detection-hackathon/blob/main/arch.jpg)


## Steps to test

Steps for testing the system:
1. Click on the circuit simulation link (https://wokwi.com/projects/415272090827317249). On the right hand side panel, it displays the circuit with a play button on the top left of the panel.
2. Click the button. This should start the simulation, which primarily consists of setting up Wi-Fi for the ESP32, establishing an MQTT connection to the publicly available Eclipse Mosquitto broker. [Learn more here](https://test.mosquitto.org/)
3. A console opens up in the bottom of the circuit. It displays the stage of simulation. Wait until it displays:
- Connected to Wi-Fi (with a MAC address)
- Connected to MQTT Broker
- Subscribed to topic: save-the-stray/INDCYC
4. Once the simulation is set up successfully and running, go to the website hosting the application (http://167.71.234.184:8501/).
5. Upload an IR video for testing. The application then detects animals through an ML model in the backend, displaying logs as the animal is detected or not detected.
6. When an animal is detected, the server sends an MQTT message "on" which lights up the LED, plays sound from the buzzer and displays a message to alert drivers. When an animal is no longer detected, it deactivates the actuators and clears the OLED screen.


Made for Save The Stray Challenge: https://unstop.com/hackathons/save-the-stray-challenge-iiit-naya-raipur-1221150

Each folder has its own README explaining all of the different components of the project.
