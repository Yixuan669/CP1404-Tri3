from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that has a reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

