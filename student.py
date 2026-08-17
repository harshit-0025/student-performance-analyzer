# Student Data

name = input("Enter Name: ")
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
python = int(input("Enter Python Marks: "))
japanese = int(input("Enter Japanese Marks: "))

total_marks = maths + science + python + japanese
marks_average = total_marks / 4


def calculate_result(marks_average):
    if marks_average > 50:
        return "Pass"
    else:
        return "Fail"


def calculate_grade(total_marks):
    if total_marks > 300:
        return "A"
    elif total_marks > 230:
        return "B"
    elif total_marks > 170:
        return "C"
    else:
        return "D"


result = calculate_result(marks_average)
grade = calculate_grade(total_marks)


print("\n========== STUDENT PROFILE ==========")
print("NAME       :", name)
print("TOTAL MARKS:", total_marks, "/400")
print("PERCENTAGE :", marks_average, "%")
print("RESULT     :", result)
print("GRADE      :", grade)