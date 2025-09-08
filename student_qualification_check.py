# Author: Shawn Daumer
# Program name: student_qualification_check.py
# Desc: Checks if a student qualifies for a dean's list or honor roll based on GPA



while True:
    # Initialized variables
    last_name = ""
    first_name = ""
    gpa = 0.0

    print("What is the student's last name?")
    last_name = input()
    if last_name == "ZZZ":
        exit()
    print("\n What is the student's first name?")
    first_name = input()
    print("\n What is the student's GPA?")
    gpa = float(input())

    if gpa >= 3.5:
        print(f"\n {first_name} {last_name} qualifies for the Dean's List.")
    elif gpa >= 3.25:
        print(f"\n {first_name} {last_name} qualifies for Honor Roll.")

