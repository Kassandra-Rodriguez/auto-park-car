from picarx import Picarx
import time
from vilib import Vilib
import cv2
import numpy as np


def is_parking_spot_empty(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of color you're interested in
    # Example: detect light gray color; adjust the range based on your specific needs
    lower_bound = np.array([0, 0, 200])  # Lower HSV boundary
    upper_bound = np.array([180, 25, 255])  # Upper HSV boundary

    # Create a mask to extract regions of interest
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Calculate the percentage of the area covered by the detected color
    coverage_ratio = np.sum(mask > 0) / mask.size

    # Assume spot is empty if the detected color covers more than 30% of the image
    return coverage_ratio > 0.3


def confirm_parking_spot(px):
    """
    Confirm there's a parking spot by turning the camera right
    and potentially using the camera feed for confirmation.
    """
    # Angle to turn camera to the right; adjust based on your setup
    right_angle = 85
    px.set_cam_pan_angle(right_angle)
    time.sleep(1)  # Wait for a moment to stabilize the camera
    
    # Insert logic here to use the camera feed for final confirmation
    
    print("Potential empty spot detected. Capturing image for confirmation.")
    px.stop()  # Stop the car if a spot is detected
    _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    path = "/home/kassandrarodriguez/auto-park-car/photos/"
    Vilib.take_photo(str(_time), path)
    image_path = f"{path}/{_time}.jpg"
    print(f"The photo saved as: {image_path}")
    # Here you would add the logic to process the image and confirm the spot is empty
    # Example usage

    if is_parking_spot_empty(image_path):
        print("The parking spot is empty.")
    else:
        print("The parking spot is not empty.")
        
        return

def find_parking_spot(px, distance_threshold):
    px.backward(speed=1)  # Move forward at a slow speed
    try:
        while True:
            distance = px.ultrasonic.read()  # Get the distance reading
            print(f"Distance: {distance} cm")
            if distance > distance_threshold:
                print("Potential empty spot detected.")
                px.backward(0)  # Stop the car
                
                
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
        px.set_cam_pan_angle(0)
        px.backward(0)  # Stop the car
        Vilib.camera_close()  # Turn off the camera when done
