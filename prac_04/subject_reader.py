"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)
    display_subject_details(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data

def display_subject_details(data):
    """Display each subject's details nicely formatted."""
    for subject, lecturer, student_count in data:
        print(f"{subject} is taught by {lecturer} and has {student_count} students")


main()