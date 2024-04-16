from picarx import Picarx
import time
from vilib import Vilib

def confirm_parking_spot(px):
    """
    Confirm there's a parking spot by turning the camera right
    and potentially using the camera feed for confirmation.
    """
    # Angle to turn camera to the right; adjust based on your setup
    right_angle = 35
    px.set_camera_servo1_angle(right_angle)
    time.sleep(1)  # Wait for a moment to stabilize the camera
    
    # Insert logic here to use the camera feed for final confirmation

def find_parking_spot(px, distance_threshold):
    px.forward(speed=10)  # Move forward at a slow speed
    try:
        while True:
            distance = px.ultrasonic.read()  # Get the distance reading
            print(f"Distance: {distance} cm")
            if distance > distance_threshold:
                print("Potential empty spot detected.")
                px.forward(0)  # Stop the car
                confirm_parking_spot(px)
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Manual interruption. Stopping the car.")
    finally:
        px.stop()
        print("Finished scanning for parking spots.")

if __name__ == "__main__":
    try:
        px = Picarx()
        
        # Initialize the camera
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        
        # Define the threshold for detecting a parking spot
        distance_threshold = 20  # You might need to adjust this value
        
        find_parking_spot(px, distance_threshold)
        
    finally:
        # Clean up and reset camera servos to default position
        px.set_camera_servo1_angle(0)
        px.set_camera_servo2_angle(0)
        px.forward(0)  # Stop the car
        Vilib.camera_close()  # Turn off the camera when done
