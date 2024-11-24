import streamlit as st
import paho.mqtt.client as mqtt
import os
import tempfile
import glob
from ultralytics import YOLO
import subprocess
import cv2
import time


MODEL_PATH = "/home/sarthak/animal_detection_and_warning_system/best.pt"  
SAVE_DIR = "/home/sarthak/animal_detection_and_warning_system/runs/detect" 
os.makedirs(SAVE_DIR, exist_ok=True)


MQTT_BROKER = "test.mosquitto.org"  
MQTT_PORT = 1883  
MQTT_TOPIC = "testicals/topic" 


model = YOLO(MODEL_PATH)


def publish_message(message):
    try:
        client = mqtt.Client()
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
        client.loop_start()
        client.publish(MQTT_TOPIC, payload=message, qos=1)
        client.loop_stop()
        client.disconnect()
        st.success(f"Message '{message}' sent successfully!")
    except Exception as e:
        st.error(f"Failed to send message: {str(e)}")


def convert_to_mp4(input_path, output_path):
    try:
        subprocess.run(
            ["ffmpeg", "-i", input_path, "-vcodec", "libx264", "-acodec", "aac", output_path],
            check=True
        )
        return output_path
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to convert video: {e}")
        return None

def display_real_time_video(video_path):
    st.write("### Real-Time Video Display")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        st.error("Failed to open the video for real-time display.")
        return

   
    stframe = st.empty()  
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.1)  
            continue

        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_container_width=True)

       
        if not os.path.exists(video_path): 
            break

    cap.release()


st.title("Animal Detection and Warning System")
st.write("This application detects animals in uploaded videos using thermal sensors and a trained ML model, triggering deterrents when necessary.")


if st.button("Detect Animal", key="detect_animal"):
    publish_message("on")  

if st.button("Turn Off", key="turn_off"):
    publish_message("off")  


st.write("### Upload a video for animal detection")
uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
if uploaded_video is not None:
    temp_video_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video_file.write(uploaded_video.read())
    temp_video_file.close()

    st.info("Processing the video through the YOLO model. Please wait...")

    try:
        consecutive_with_dog = 0
        consecutive_without_dog = 0
        DOG_CLASS_ID = 0  
        CONFIDENCE_THRESHOLD = 0.5 

        results = model.track(
            source=temp_video_file.name,
            stream=True,  
            show=False,
            save=True,
            save_txt=False,
            save_dir=SAVE_DIR
        )

        stframe = st.empty()  
        for result in results:
            detections = result.boxes.data.cpu().numpy()  
            has_dog = False

            for d in detections:
                class_id = int(d[5])  
                confidence = d[4]  

                if class_id == DOG_CLASS_ID and confidence > CONFIDENCE_THRESHOLD:
                    has_dog = True
                    break 

            if has_dog:
                consecutive_with_dog += 1
                consecutive_without_dog = 0
            else:
                consecutive_without_dog += 1
                consecutive_with_dog = 0

            if consecutive_with_dog == 10:
                publish_message("on")
            elif consecutive_without_dog == 10:
                publish_message("off")

            frame = result.orig_img  
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            stframe.image(frame_rgb, channels="RGB", use_container_width=True)
        
        
        publish_message("off")

        st.success("Video processing completed successfully!")

        processed_dirs = sorted(glob.glob(f"{SAVE_DIR}/*"), key=os.path.getctime, reverse=True)
        if not processed_dirs:
            raise FileNotFoundError("No processed directories found!")
        processed_dir = processed_dirs[0]  

        processed_video_path = glob.glob(f"{processed_dir}/*.avi")
        if not processed_video_path:
            raise FileNotFoundError("Processed video file not found!")
        processed_video_path = processed_video_path[0]  
        
        mp4_video_path = os.path.join(processed_dir, "output.mp4")
        converted_video_path = convert_to_mp4(processed_video_path, mp4_video_path)
                

        if converted_video_path:
            st.success(f"Video processed and converted successfully! Path: {converted_video_path}")

            st.write("### Processed Video")
            with open(converted_video_path, "rb") as processed_file:
                st.video(processed_file.read())  

    except Exception as e:
        st.error(f"Failed to process video: {str(e)}")
