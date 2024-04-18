from picarx import Picarx
import time
from vilib import Vilib
import cv2
import numpy as np
import matplotlib.pyplot as plt

def is_parking_spot_empty(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found or cannot be loaded.")
        return False

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 50])  # Adjust these values based on the actual blue tape color
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)
    mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    coverage_ratio = np.sum(mask_cleaned > 0) / mask_cleaned.size

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('HSV Mask')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(mask_cleaned, cmap='gray')
    plt.title('Cleaned Mask')
    plt.axis('off')

    plt.show()

    return coverage_ratio > 0.05  # Adjust this threshold as needed

def confirm_parking_spot(px):
    right_angle = 90
    down_angle = -20  # Tilt the camera down to focus on the ground
    px.set_cam_pan_angle(right_angle)
    px.set_cam_tilt_angle(down_angle)
    time.sleep(1)  # Wait for the camera to stabilize

    print("Camera adjusted, capturing image for confirmation.")
    _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    path = "/home/kassandrarodriguez/auto-park-car/photos/"
    Vilib.take_photo(str(_time), path)
    image_path = f"{path}/{_time}.jpg"
    print(f"The photo saved as: {image_path}")

    if is_parking_spot_empty(image_path):
        print("The parking spot is empty.")
        # Drive into the parking spot
        px.forward(speed=2)
        time.sleep(0.4)
        px.set_dir_servo_angle(25)  # Steer right, adjust angle based on need
        time.sleep(0.5)  # Give a moment for the car to align
        px.backward(speed=1)  # Adjust speed as necessary
        time.sleep(4)  # Adjust duration based on the distance to fully enter the spot
        px.stop()
        px.set_dir_servo_angle(0)  # Reset steering angle
    else:
        print("The parking spot is not empty.")

def find_parking_spot(px, distance_threshold):
    px.backward(speed=1)
    try:
        while True:
            distance = px.ultrasonic.read()
            if distance > distance_threshold:
                print("Potential empty spot detected.")
                px.backward(0)  # Stop the car
                confirm_parking_spot(px)
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Manual interruption.")
    finally:
        px.stop()
        print("Finished scanning for parking spots.")

if __name__ == "__main__":
    try:
        px = Picarx()
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        distance_threshold = 20
        find_parking_spot(px, distance_threshold)
    finally:
        px.set_cam_pan_angle(0)
        px.set_cam_tilt_angle(0)
        px.stop()
        Vilib.camera_close()
