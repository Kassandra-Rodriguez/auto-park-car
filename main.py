from picarx import Picarx
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time


# Initialize the PiCar-X
pcx = Picarx()

# Initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(640, 480))

def find_parking_spot(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Here you can insert more complex image processing to detect parking lines
    # For now, let's just simulate that we always find a spot
    return True

try:
    # Start driving forward
    pcx.backward(speed=50)  # Adjust speed as needed

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        
        # Check for parking spots
        if find_parking_spot(image):
            print("Parking spot found!")
            pcx.stop()  # Stop the car
            break
        
        # Clear the stream for the next frame
        rawCapture.truncate(0)

except KeyboardInterrupt:
    pcx.stop()  # Ensure the car stops if the script is interrupted
