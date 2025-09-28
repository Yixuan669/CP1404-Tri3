MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Get the choice from the user and do the task related to the choice input"""
    choice = " "
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_level(score)
            print(result)
        elif choice == "S":
            print_star(score)
        elif choice == "Q":
            print("Farewell")
        else:
            print("Invalid choice")


def get_valid_score():
    """Get the score from the user"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_level(score):
    """Determine the level of the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_star(score):
    """Display the star related to the score"""
    print("*" * score)

main()