"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data(FILENAME)
    display_subject_details(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display subject details."""
    for subject in subjects:
        subject_code = subject[0]
        lecturer = subject[1]
        student_count = subject[2]
        print(f"{subject_code}is taught by {lecturer}and has {student_count} students.")



main()
