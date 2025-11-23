from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised taxi with fanciness and flagfall"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise the SilverServiceTaxi"""

        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness