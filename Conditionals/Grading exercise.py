# A more complex exercise 1
Exam_score = int(input("Exam score: "))
Assignment_Score = int(input("Assignment score: "))
Attendance_percentage = int(input("Attendance percentage: "))

if Exam_score < 40:
    print(f"Your Exam score was {Exam_score} and it wasn't enough to pass. Your grade is F")

elif Exam_score >= 40 and 50 <= Assignment_Score < 90:
    print(f"Your Exam score was {Exam_score} and Assignment score was {Assignment_Score}. You pass with a grade P")

elif Exam_score >= 40 and Assignment_Score < 50 and Attendance_percentage < 75:
    print(f"Your Exam score was {Exam_score}, Assignment score was {Assignment_Score} and Attendance Percentage was {Attendance_percentage}%. You fail with grade F")

elif Exam_score >= 90 and Assignment_Score >= 70 and Attendance_percentage >= 90:
    print(f"Your Exam score was {Exam_score}, Assignment score was {Assignment_Score} and Attendance percentage was {Attendance_percentage}%. Congratulations, you passed with a Grade A")
else:
    print("Grade C")
