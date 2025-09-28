"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    """Get score and generate a random score, determine the status and display the status"""
    score = float(input("Enter score: "))
    random_score = random.randint(1, 100)
    score = determine_level(score)
    print(score)
    print(random_score, score)



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

main()