from guitar import Guitar

def main():
    """Main function to manage the list of guitars."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("These are my guitars:")
    display_guitars(guitars)

    # Sort by year
    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    # Add new guitars from user
    add_new_guitars(guitars)

    # Save all guitars back to file
    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}")

def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars