from gpiozero import Servo
from time import sleep
from picarx import Picarx
from vilib import Vilib


# Initialize PiCar-X and Vilib
pcx = Picarx()
Vilib.camera_start()
Vilib.detect_color_name('blue')

# Define servos for pan and tilt using GPIO Zero
tilt_servo = Servo(17)  # GPIO pin 17 corresponds to P1 on the Robot HAT
pan_servo = Servo(27)  # GPIO pin 27 corresponds to P2 on the Robot HAT

# Function to tilt the camera
def tilt_camera(angle):
    """
    Tilts the camera to the given angle.
    Parameters:
        angle (float): The angle to tilt the camera. Ranges from -1 to 1.
                       -1 is full one direction, 1 is full the other direction.
    """
    tilt_servo.value = angle
    sleep(0.5)  # Give the servo time to move

# Use the function to tilt the camera right
# Assuming the right direction is somewhere between 0 and 1
tilt_camera(0.5)  

def search_for_parking():
    # parking spot search code here
    pass


try:
    search_for_parking()
except KeyboardInterrupt:
    print("Interrupted, stopping the car.")
    pcx.stop()
finally:
    Vilib.camera_close()
    print("Exiting the script.")

