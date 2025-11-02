from guitar import Guitar


def main():
    print("My guitars!")

    guitars = []

    name = input("Name: ").strip()
    while name != "":
        try:
            year = int(input("Year: ").strip())
        except ValueError:
            print("Invalid year; please enter an integer.")
            continue
        try:
            cost_str = input("Cost: $").strip()
            cost = float(cost_str)
        except ValueError:
            print("Invalid cost; please enter a number.")
            continue

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

        name = input("Name: ").strip()

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_str}")


if __name__ == "__main__":
    main()