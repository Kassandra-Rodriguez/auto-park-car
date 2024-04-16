from picarx import Picarx
import time

def test_ultrasonic_sensor():
    px = Picarx()  # Initialize the Picar-x
    try:
        while True:
            distance = px.ultrasonic.read()  # Read the distance measurement from the ultrasonic sensor
            print(f"Distance: {distance} cm")  # Print the distance
            time.sleep(1)  # Wait for 1 second before the next read
    except KeyboardInterrupt:
        print("Stopping ultrasonic sensor test.")
    finally:
        # Insert the cleanup code here
        px.cleanup()  # Replace this with the actual cleanup method if it's different.
        print("GPIO pins have been cleaned up.")

if __name__ == "__main__":
    test_ultrasonic_sensor()
