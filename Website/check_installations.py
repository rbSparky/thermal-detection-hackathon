try:
    import matplotlib
    print(f"matplotlib version: {matplotlib.__version__}")
except ImportError:
    print("matplotlib is not installed.")

try:
    import cv2
    print(f"OpenCV version: {cv2.__version__}")
except ImportError:
    print("OpenCV (cv2) is not installed.")

try:
    from ultralytics import YOLO
    print("ultralytics is installed.")
except ImportError:
    print("ultralytics is not installed.")
