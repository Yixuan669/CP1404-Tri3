from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that has a reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on distance."""

        random_chance = randint(0, 100)

        if random_chance <= self.reliability:
            return super().drive(distance)
        else:
            return 0