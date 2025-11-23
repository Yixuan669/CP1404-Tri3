from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fares."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18km trip: ${fare:.2f}")