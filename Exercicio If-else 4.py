# Exercise 4: Grading System
# Write a program that takes a score as input from the user and prints the grade based on the following criteria:
# 90 or above: "A"
# 80 to 89: "B"
# 70 to 79: "C"
# 60 to 69: "D"
# Below 60: "F"

score = int(input("Score: "))

if score >= 90:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
else:
    print("Grade F")
