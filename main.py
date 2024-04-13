from picarx import Picarx
import time

def main():
    # Initialize the PiCar-X
    pcx = Picarx()

    try:
        # Drive forward
        print("Driving forward...")
        pcx.backward(speed=50)  # Adjust speed as necessary
        time.sleep(2)  # Adjust time to control how long it drives forward

        # Stop the car
        pcx.stop()
        print("Stopping the car...")

        # Turn right
        print("Turning right...")
        pcx.set_dir_servo_angle(10)  # Adjust the angle to control the sharpness of the turn
        pcx.forward(speed=50)  # Continue driving forward while the wheels are turned
        time.sleep(1)  # Adjust time to control the duration of the turn

        # Stop the car after the turn
        pcx.stop()
        print("Stopping the car after the turn...")

    finally:
        # Reset the steering angle and stop the car
        pcx.set_dir_servo_angle(0)
        pcx.stop()
        print("Car is stopped and steering reset.")

if __name__ == "__main__":
    main()
