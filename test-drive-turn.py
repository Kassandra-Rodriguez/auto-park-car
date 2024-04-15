from picarx import Picarx
import time
from vilib import Vilib

def look_for_parking(px):
    # Drive forward at low speed to scan for parking spots
    px.backward(1)
    try:
        # Scan for an available parking spot
        while True:
            distance = px.ultrasonic.read()
            print("Scanning... Distance: ", distance, "cm")
            
            # Assume if distance is greater than a threshold, we may have a spot
            if distance > 40:  # Threshold distance in cm to consider it might be a spot
                print("Potential spot detected.")
                px.stop()
                
                # Turn the camera to the right to check the spot
                px.set_cam_pan_angle(95)  # Tilt camera to right to check the spot
                
                
                
                time.sleep(1)  # Give camera time to adjust and stream
                if Vilib.check_if_spot_is_empty():  # This is a placeholder for your spot checking logic
                    print("Spot is empty. Proceed to park.")
                    px.stop()
                    # Add your parking logic here
                    break
                else:
                    print("Spot is not empty. Continue scanning.")
                    px.backward(10)
            
            time.sleep(0.5)  # Small delay to continuously check for spots

    finally:
        # Stop the car and reset the camera position once done or if an error occurs
        px.stop()
        px.set_cam_pan_angle(0)  # Reset camera to forward position

if __name__ == "__main__":
    try:
        px = Picarx()
        # Start camera stream with vilib (you need to start this beforehand and implement the method check_if_spot_is_empty)
        Vilib.camera_start(vflip=False,hflip=False) # vflip:vertical flip, hflip:horizontal Flip
        Vilib.display(local=True,web=True) 
        Vilib.color_detect(color="blue")  # Start color detection (placeholder for your logic to confirm empty spot)
        look_for_parking(px)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if px:
            px.stop()  # Ensure the car is stopped
            px.set_cam_pan_angle(0)  # Reset camera to default position
        print("Operation completed.")
