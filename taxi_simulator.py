from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Run the taxi simulator."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0

    MENU = "q)uit, c)hoose taxi, d)rive"
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            # 选择出租车
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                except ValueError:
                    distance = 0
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display all taxis with their index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")