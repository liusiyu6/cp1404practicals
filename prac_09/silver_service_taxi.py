"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Multiply price_per_km by fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string with flagfall displayed."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
