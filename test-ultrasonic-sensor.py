from robot_hat import Ultrasonic
import time

def test_ultrasonic_sensor(ultrasonic):
    try:
        while True:
            distance = ultrasonic.get_distance()  # Use the appropriate method to read the distance
            print(f"Distance: {distance} cm")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping ultrasonic sensor test.")
    finally:
        # Add any cleanup code if necessary for your ultrasonic sensor library
        print("Ultrasonic sensor test completed.")

if __name__ == "__main__":
    ultrasonic = None
    try:
        ultrasonic = Ultrasonic()  # Initialize the Ultrasonic sensor
        test_ultrasonic_sensor(ultrasonic)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # If there's any cleanup for the ultrasonic sensor specifically, do it here
        print("Operation completed.")
