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