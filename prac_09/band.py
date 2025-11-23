from musician import Musician

class Band:
    """A class to represent a band."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []