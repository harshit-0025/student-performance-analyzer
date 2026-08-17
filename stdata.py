# Student Performance Analyzer

students = []


def calc_grade(total):
    if total > 300:
        return "A"

    elif total > 200:
        return "B"

    else:
        return "C"


def calc_result(marks_avg):
    if marks_avg > 40:
        return "PASS"

    else:
        return "FAIL"


for i in range(5):
    print("\n=========== STUDENT", i + 1, "===========")

    name = input("Enter Name: ")

    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    python = int(input("Enter Python Marks: "))

    total = math + science + english + python
    marks_avg = total / 4

    grade = calc_grade(total)
    result = calc_result(marks_avg)

    student = {
        "name": name,
        "total": total,
        "marks_avg": marks_avg,
        "grade": grade,
        "result": result
    }

    students.append(student)


print("\n\n========== ALL STUDENTS ==========")

for student in students:
    print(
        student["name"],
        "| Total:", student["total"],
        "| Average:", student["marks_avg"],
        "| Result:", student["result"],
        "| Grade:", student["grade"]
    )


highest_student = max(students, key=lambda x: x["total"])


print("\n========== HIGHEST SCORER ==========")

print("Name:", highest_student["name"])
print("Total Marks:", highest_student["total"])
print("Average:", highest_student["marks_avg"])
print("Grade:", highest_student["grade"])