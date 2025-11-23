"""
CP1404/CP5632 Practical
UnreliableCar Test
"""

from unreliable_car import UnreliableCar

test_car = UnreliableCar("Unreliable", 100, 50)

for i in range(10):
    distance = test_car.drive(10)
    print(f"Attempt {i + 1}: drove {distance} km")
