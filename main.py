from picarx import Picarx
from vilib import Vilib
import time

# Initialize the PiCar-X
pcx = Picarx()

# Start the camera and color detection
Vilib.camera_start()
Vilib.detect_color_name('blue')  # Assuming 'blue' is a pre-defined color

def search_for_parking():
    # Tilt the camera to the right to check for parking space
    # Adjust the angle as needed for your setup
    pcx.set_cam_pan_angle(30)  
    pcx.set_cam_tilt_angle(0)  # Assuming straight ahead is 0 degrees
    
    time.sleep(1)  # Give the camera time to move

    # check the camera feed to determine if there is a parking spot
    # For now, let's assume we have a function that returns True if a parking spot is available
    if is_parking_spot_available():
        print("Parking spot found!")
        pcx.stop()  # Stop the car or initiate parking maneuver
    else:
        # No suitable parking spot found, keep driving
        pcx.forward(20)  # Continue driving forward at a slow speed
    
    # Reset camera pan/tilt to default positions
    pcx.set_cam_pan_angle(0)
    pcx.set_cam_tilt_angle(0)
    time.sleep(0.1)  # Allow a short delay for the camera to reset

def is_parking_spot_available():
    # Placeholder function for parking spot detection logic
    # implement the actual logic using Vilib's color detection
    return False

try:
    # Start searching for a parking spot
    while True:
        search_for_parking()
except KeyboardInterrupt:
    # Handle any cleanup on interrupt
    print("Interrupted, stopping the car.")
    pcx.stop()
finally:
    # Cleanup
    Vilib.camera_close()
    print("Exiting the script.")
