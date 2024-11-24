# Animal Detection and Warning System

This project is an **Animal Detection and Warning System** implemented using **YOLO** (You Only Look Once) for real-time object detection, and **Streamlit** for the user interface. It detects the presence of animals, particularly dogs, in a video stream and triggers warning signals through MQTT based on consecutive detection.

## Features

- **Real-time Object Detection**: Uses the YOLO model to detect objects in video streams.
- **Animal Detection**: Specifically detects dogs using the YOLO model.
- **Warning System**: Sends MQTT messages to trigger a warning system when a dog is detected for consecutive frames.
- **User Interface**: Streamlit is used for creating the front-end to interact with the system and visualize the processed video.
- **Hardware Integration**: Includes an MQTT-based circuit simulation using [Wokwi](https://wokwi.com/) for LED display and sound buzzer warnings.

## Technologies Used

- **YOLOv8**: For object detection.
- **Streamlit**: For creating the web-based interface.
- **MQTT**: For sending warnings and messages based on detection.
- **Python**: Main programming language for implementing the backend logic.
- **Ultralytics**: For YOLO model implementation and inference.
- **OpenCV**: For handling video processing and manipulation.
- **Wokwi**: For simulating hardware components like LED screens and buzzers.
- **Git**: For version control.

## Setup

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/srthkaggrwl/Animal_Detection_and_Warning_System.git
cd Animal_Detection_and_Warning_System
```

### 2. Create a Virtual Environment

It's recommended to create a Python virtual environment for managing dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the core dependencies directly:

```bash
pip install streamlit ultralytics paho-mqtt opencv-python
```

### 4. Run the Streamlit App

To run the Streamlit application, use the following command:

```bash
streamlit run streamlit_app.py
```

### 5. Access the Application

Once the app starts, you can access it on your browser:

- **Local URL**: `http://localhost:8501`
- **Network URL**: `http://<your-server-ip>:8501`

The working application is hosted on the following URL - http://167.71.234.184:8501/
## How It Works

1. **Video Input**: Users upload a video to the Streamlit app.
2. **Real-time Detection**: The video is processed frame by frame, and YOLO detects objects in each frame.
3. **Dog Detection**: The system specifically checks for the presence of a dog in the frames.
4. **Consecutive Detection**: If a dog is detected consecutively for 10 frames, an MQTT message is sent with the `"on"` signal to trigger a warning. If no dog is detected for 10 frames, an `"off"` signal is sent.
5. **Live Video Stream**: The processed video with detected objects is displayed to the user.
6. **Hardware Simulation**: The MQTT messages are received by a Wokwi circuit that acts as a subscriber.

## MQTT Integration with Wokwi Simulation

This project integrates with a Wokwi simulation that serves as a hardware demonstration for the warning system:

- The Wokwi circuit contains:
  - An **LED screen** that displays the message: **"ANIMAL DETECTED DRIVE SLOW!!!"**.
  - A **sound buzzer** that activates when a warning signal is received.
- **MQTT Roles**:
  - The **Streamlit application** acts as the **publisher**.
  - The **Wokwi circuit** acts as the **subscriber**.
- **Signal Behavior**:
  - An **"on"** signal triggers the LED display and buzzer.
  - An **"off"** signal turns them off.

You can view the Wokwi simulation for this project at the following link:

👉 [Wokwi Simulation: Animal Warning System](https://wokwi.com/projects/415272090827317249)

### MQTT Configuration

To set up MQTT, ensure you replace the MQTT broker details in the code:

```python
mqtt_broker = "your_broker_ip"
mqtt_port = 1883
mqtt_topic = "animal_warning"
```

## File Structure

```plaintext
.
├── .gitignore            # Git ignore file
├── best.pt               # YOLO model weights
├── check_installations.py # Script to check required installations
├── package.json          # Package management for frontend
├── streamlit_app.py      # Main Streamlit application file
```

## Troubleshooting

- **ModuleNotFoundError**: Ensure that all required dependencies are installed in the virtual environment.
  
  Example:
  ```bash
  python check_installations.py
  ```

- **No Detection**: If no dogs are detected, ensure that the YOLO model is correctly loaded and that the model weights (`best.pt`) are available in the specified directory.

- **MQTT Connection Issues**: Ensure that the MQTT broker is correctly configured and accessible from both the Streamlit application and the Wokwi circuit.
