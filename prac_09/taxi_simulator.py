"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    bill_to_date = 0.0
    current_taxi = None

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == "q":
            break

        elif choice == "c":
            current_taxi = choose_taxi(taxis)

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Let user choose a taxi; return selected taxi or None."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        return taxis[choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Drive the taxi and return the trip cost."""
    distance = int(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare


def display_taxis(taxis):
    """Print taxis with numbering."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
