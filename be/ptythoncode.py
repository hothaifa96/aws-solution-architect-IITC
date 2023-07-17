import random


class Car:
    def accelerate(self):
        random_num = random.randint(100, 140)
        print(f"The speed of the car is {random_num} kph")

    def apply_brakes(self):
        random_num = random.randint(20, 40)
        print(f"The speed of the car is {random_num} kph")

    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")


class Motorcycle:
    def rev(self):
        random_num = random.randint(100, 140)
        print(f"The speed of the motorcycle is {random_num} kph")

    def pull_brake_lever(self):
        random_num = random.randint(20, 40)
        print(f"The speed of the motorcycle is {random_num} kph")

    def assign_rider(self, rider_name):
        print(f"{rider_name} is driving the motorcycle")


class Vehicle:
    vehicles = []

    def __init__(self, v=None):
        if v ==None:
            vc=Vehicle(Car())
            vm=Vehicle(Motorcycle())
        self.v = v
        Vehicle.vehicles.append(self)


    def newDriver(self, driver_name):
        if isinstance(self.v, Car):
            self.v.assign_driver(driver_name)
        elif isinstance(self.v, Motorcycle):
            self.v.assign_rider(driver_name)

        # for v in self.vehicles:
        #     if isinstance(v,Car):
        #         v.assign_driver(driver_name)
        #     elif isinstance(self.vehicle, Motorcycle):
        #         v.assign_rider(driver_name)

    def speedUp(self):
        if isinstance(self.v, Car):
            self.v.accelerate()
        elif isinstance(self.v, Motorcycle):
            self.v.rev()

    def slowdown(self):
        if isinstance(self.v, Car):
            self.v.apply_brakes()
        elif isinstance(self.v, Motorcycle):
            self.v.pull_brake_lever()


v = Vehicle()
vehicles=v.vehicles
# vehicles[0].newDriver('israel')
# Perform actions on each vehicle in the list
for v in vehicles:
    v.newDriver("Israel")
    v.speedUp()
    v.slowdown()
    print('\n')
