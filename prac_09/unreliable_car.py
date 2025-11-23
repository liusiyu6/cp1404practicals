"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from car import Car
import random


class UnreliableCar(Car):
    """A car that sometimes does not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with reliability (0–100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if a random number is less than reliability."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0  # did not drive
