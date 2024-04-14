from picarx import Picarx
import time

def scan_for_parking(px, pan_angle=35):
    """
    Pans the camera to scan for parking spots.

    :param px: The Picarx instance.
    :param pan_angle: The angle to pan to the right for scanning.
    """
    # Tilt the camera down a bit to see the parking spots better
    px.set_camera_servo2_angle(-20)
    time.sleep(1)
    
    # Start by looking straight ahead
    px.set_camera_servo1_angle(0)
    time.sleep(1)
    
    # Pan to the right to scan for parking spots
    for angle in range(0, pan_angle + 1):
        px.set_camera_servo1_angle(angle)
        time.sleep(0.01)
        
        # add logic to check for a parking spot.

    
    # Reset camera position back to straight ahead
    px.set_camera_servo1_angle(0)
    time.sleep(1)
    
    # Reset camera tilt to original position
    px.set_camera_servo2_angle(0)
    time.sleep(1)

if __name__ == "__main__":
    try:
        px = Picarx()
        px.forward(30)  # Drive forward at speed 30
        time.sleep(0.5)
        
        # scan for parking while driving
        scan_for_parking(px, pan_angle=35)
        
        px.forward(0)  # Stop the car
        time.sleep(1)
        
    finally:
        px.forward(0)  # Ensure the car stops if the script is interrupted
