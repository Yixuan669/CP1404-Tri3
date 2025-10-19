import csv
FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon_data(FILENAME)
    champion_to_count = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champion_to_count.items():
        print(f"{champion:20} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def read_wimbledon_data(FILENAME):
    """Read Wimbledon data from CSV and return a list of records (each as a list)."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = [row for row in reader]
    return data


def count_champions(data):
    """Return a dictionary with champion names as keys and win counts as values."""
    champion_to_count = {}
    for record in data:
        champion = record[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def get_countries(data):
    """Return a sorted set of all unique champion countries."""
    countries = {record[1] for record in data}
    return sorted(countries)

main()