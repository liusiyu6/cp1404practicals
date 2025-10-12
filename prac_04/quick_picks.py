import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate quick picks (lotto numbers)."""
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate one quick pick (6 unique sorted numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:  # ensure no duplicates
            numbers.append(number)
    numbers.sort()  # ascending order
    return numbers


def print_quick_pick(numbers):
    """Print the quick pick neatly formatted."""
    for number in numbers:
        print(f"{number:2}", end=" ")  # align numbers in 2-character columns
    print()  # new line after each quick pick


main()
