from guitar import Guitar


def main():
    # Test data
    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    TEST_YEAR = 2022

    print(f"{l5.name} get_age() - Expected 100. Got {l5.get_age(TEST_YEAR)}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age(TEST_YEAR)}")

    print(f"{l5.name} is_vintage() - Expected True. Got {l5.is_vintage(TEST_YEAR)}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage(TEST_YEAR)}")


if __name__ == "__main__":
    main()