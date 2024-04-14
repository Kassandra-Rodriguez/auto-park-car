from picarx import Picarx
import time
from vilib import Vilib

def scan_for_parking(px, pan_angle=35):
    """
    Pans the camera to scan for parking spots.

    :param px: The Picarx instance.
    :param pan_angle: The angle to pan to the right for scanning.
    """
    # Tilt the camera down a bit to see the parking spots better
    px.set_camera_servo1_angle(-20)
    time.sleep(1)
    
    # Start by looking straight ahead
    px.set_camera_servo1_angle(0)
    time.sleep(1)
    
    # Pan to the right to scan for parking spots
    for angle in range(0, pan_angle + 1):
        px.set_camera_servo1_angle(angle)
        time.sleep(0.01)
        
        # logic to process the video feed and check for a parking spot
    
    # Reset camera position back to straight ahead
    px.set_camera_servo1_angle(0)
    time.sleep(1)
    
    # Reset camera tilt to original position
    px.set_camera_servo2_angle(0)
    time.sleep(1)

if __name__ == "__main__":
    try:
        # Initialize the PiCar-X and Vilib
        px = Picarx()
        
        # Start the Vilib video stream and display
        Vilib.camera_start(vflip=False,hflip=False) # vflip:vertical flip, hflip:horizontal Flip
        # local:local display, web:web display
        # when local=True, the image window will be displayed on the system desktop
        # when web=True, the image window will be displayed on the web browser at http://localhost:9000/mjpg
        Vilib.display(local=True,web=True) 
    
        
        px.backward(30)  # Drive forward at speed 30
        time.sleep(0.5)
        
        # Now let's scan for parking while driving
        scan_for_parking(px, pan_angle=35)
        
        px.backward(0)  # Stop the car
        time.sleep(1)
        
    finally:
        px.backward(0)  # Ensure the car stops if the script is interrupted
        # Vilib.camera_close()  # Stop the camera stream and close the display window
