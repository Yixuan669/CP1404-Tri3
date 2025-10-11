import random

NUMBER_PER_PICKS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    number_of_picks = int(input('Number of picks: '))
    for i in range(number_of_picks):
        quick_pick = generate_quick_picks()
        print(" ".join(f'{number:2}' for number in quick_pick))

def generate_quick_picks():
    numbers = []
    while len(numbers) < NUMBER_PER_PICKS:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers
main()