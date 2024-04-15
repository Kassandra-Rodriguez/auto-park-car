from picarx import Picarx
import time

def look_for_parking(px):
    # Tilt camera to the right to start looking for a parking spot
    px.set_cam_pan_angle(45)  # Adjust this angle based on your setup
    
    # Drive forward while the camera is tilted
    px.forward(30)  # Set speed; adjust based on your need
    
    # Assuming detection logic is handled elsewhere and triggers a stop
    try:
        while True:
            # Here you would typically check for parking spot detection
            # For demonstration, let's just run this for a few seconds
            time.sleep(10)
            break
    finally:
        # Stop the car and reset the camera position once done or if an error occurs
        px.stop()
        px.set_cam_pan_angle(0)  # Reset camera to forward position

if __name__ == "__main__":
    px = None
    try:
        px = Picarx()
        look_for_parking(px)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if px:
            px.stop()  # Ensure the car is stopped
            px.set_cam_pan_angle(0)  # Reset camera to default position
        print("Operation completed.")
