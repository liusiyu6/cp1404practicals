def main():
    score = get_valid_score()  # 进入菜单前先获取一个有效分数

    MENU = """Menu:
G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Score: {score} -> {result}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell! Thanks for using the program.")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
