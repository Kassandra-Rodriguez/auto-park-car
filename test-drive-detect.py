from picarx import Picarx
import time

def find_parking_spot(px, distance_threshold):
    try:
        px.backward(speed=1)  # Set a low speed for the car to move forward slowly
        while True:
            distance = px.ultrasonic.read()  # Get distance reading from the ultrasonic sensor
            print(f"Distance: {distance} cm")
            if distance > distance_threshold:
                print("Empty spot detected.")
                px.stop()  # Stop the car if a spot is detected
                break
            time.sleep(0.5)  # Delay to avoid reading the sensor too frequently
    except KeyboardInterrupt:
        print("Manual interruption. Stopping the car.")
    finally:
        px.stop()
        print("Finished parking sequence.")

if __name__ == "__main__":
    px = None
    try:
        px = Picarx()  # Initialize the PiCar-X
        distance_threshold = 20  # Set the threshold distance to consider a spot as empty
        find_parking_spot(px, distance_threshold)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if px:
            px.stop()  # Ensure the car is stopped when the program ends
        print("Program terminated.")
