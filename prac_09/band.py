"""
CP1404/CP5632 Practical
Band class - association example
"""


class Band:
    """Band class stores a list of Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band."""
        # musicians in format: Name (list of instruments)
        musicians_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Tell each musician to play.
        If musician has no instruments → print 'needs an instrument!'
        """
        for musician in self.musicians:
            instrument = musician.get_instrument()
            if instrument:
                print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")
