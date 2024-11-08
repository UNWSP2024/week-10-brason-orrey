class Car:
    def __init__(self, year_model, make):
        # Initialize attributes for year model, make, and speed
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Speed starts at 0

    def accelerate(self):
        # Increase speed by 5
        self.__speed += 5

    def brake(self):
        # Decrease speed by 5, without going below 0
        self.__speed = max(0, self.__speed - 5)

    def get_speed(self):
        # Return the current speed
        return self.__speed

# Main program
def main():
    # Create a Car object
    my_car = Car(2015, "Subaru")

    # Accelerate the car five times, displaying speed each time
    print("Accelerating:")
    for _ in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed())

    # Brake the car five times, displaying speed each time
    print("\nBraking:")
    for _ in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed())

# Run the program
main()
