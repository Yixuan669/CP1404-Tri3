from musician import Musician

class Band:
    """A class to represent a band."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        if isinstance(musician, Musician):
            self.musicians.append(musician)
