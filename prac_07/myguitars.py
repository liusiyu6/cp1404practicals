from guitar import Guitar


def main():
    """Read guitars from file, display them, sort them, and add new ones."""
    guitars = load_guitars("guitars")
    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    print("\nAdd new guitars (press Enter to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    save_guitars("guitars", guitars)
    print("\nAll guitars saved to guitars.csv.")


def load_guitars(filename):
    """Read guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    """Write all guitars to a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Print all guitars nicely."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


if __name__ == "__main__":
    main()
