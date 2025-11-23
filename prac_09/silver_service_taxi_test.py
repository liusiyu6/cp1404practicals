"""
CP1404/CP5632 Practical
SilverServiceTaxi Test
"""

from silver_service_taxi import SilverServiceTaxi

# Example from the prac instructions
taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.drive(18)

print(taxi)
print(f"Fare: ${taxi.get_fare():.2f}")

# Assert test to ensure correctness
expected = 48.78  # from prac sheet
actual = round(taxi.get_fare(), 2)
assert actual == expected, f"Expected {expected}, got {actual}"
