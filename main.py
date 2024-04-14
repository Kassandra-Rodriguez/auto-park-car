from picarx import Picarx
import time
from vilib import Vilib

if __name__ == "__main__":
    try:
        px = Picarx()
        
        # Initialize Vilib camera
        Vilib.camera_start(vflip=False,hflip=False) # vflip:vertical flip, hflip:horizontal Flip
        # local:local display, web:web display
        # when local=True, the image window will be displayed on the system desktop
        # when web=True, the image window will be displayed on the web browser at http://localhost:9000/mjpg
        Vilib.display(local=True,web=True) 
        
        px.forward(30)
        time.sleep(0.5)
        
        # Scan for parking spots by panning the camera instead of turning the steering servo
        for angle in range(0, 35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        
        for angle in range(35, -35, -1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        
        for angle in range(-35, 0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        
        # Stop the car before tilting the camera
        px.forward(0)
        time.sleep(1)
        
        # Tilt the camera up and down to check the spots vertically
        for angle in range(0, 35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        
        for angle in range(35, -35, -1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        
        for angle in range(-35, 0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)

        # will add logic to decide if there's an available parking spot

    finally:
        # Clean up and reset camera servos to default position
        px.set_camera_servo1_angle(0)
        px.set_camera_servo2_angle(0)
        px.forward(0)  # Stop the car
