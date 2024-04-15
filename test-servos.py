from robot_hat import Pin, ADC, PWM, Servo, fileDB
from robot_hat import Grayscale_Module, Ultrasonic, utils
import time
import os

# Assuming Picarx class is already defined as you have shown

def move_camera_servos(px):
    # Sweep the pan servo from -90 to 90 degrees and back
    for angle in range(-90, 91, 5):  # Move in steps of 5 degrees
        px.set_cam_pan_angle(angle)
        time.sleep(0.1)
    
    for angle in range(90, -91, -5):  # Return to starting position
        px.set_cam_pan_angle(angle)
        time.sleep(0.1)

    # Reset pan position
    px.set_cam_pan_angle(0)

    # Sweep the tilt servo from -35 to 65 degrees and back
    for angle in range(-35, 66, 5):  # Move in steps of 5 degrees
        px.set_cam_tilt_angle(angle)
        time.sleep(0.1)
    
    for angle in range(65, -36, -5):  # Return to starting position
        px.set_cam_tilt_angle(angle)
        time.sleep(0.1)

    # Reset tilt position
    px.set_cam_tilt_angle(0)

if __name__ == "__main__":
    try:
        px = Picarx()  # Initialize the PiCar-X
        move_camera_servos(px)  # Move the camera servos
    except Exception as e:
        print("An error occurred:", e)
    finally:
        px.stop()  # Ensure motors are stopped
        print("Operation completed.")
