#Author: Shawn Daumer
#Date: 9/14/2025
#

# Part 1: 
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Part 2:
def main():
    print("Enter information about your car:")
    vehicle_type = "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors: ")
    roof = input("Enter the type of roof (e.g., sun roof, moon roof, soft top, hard top): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nCar Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

if __name__ == "__main__":
    main()


