from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fares."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18km trip: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.01, f"Expected 48.78, got {fare:.2f}"

    print("Test passed")


if __name__ == "__main__":
    main()