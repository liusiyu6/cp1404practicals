"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for num_months in range(1, num_months + 1):
        income = float(input(f"Enter income for month {num_months}: "))
        incomes.append(income)


def print_incomes_report(incomes, num_months):
    print("\nIncome Report\n-------------")
    total = 0
    for num_months in range(1, num_months + 1):
        income = incomes[num_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(num_months, income, total))


main()
