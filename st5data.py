# Student Performance Analyzer
import numpy as np

students = []

all_marks = []

def calculate_grade(total_marks):
    if total_marks > 300:
        return "A"

    elif total_marks > 200:
        return "B"

    else:
        return "C"

def calculate_result(average_marks):
    if average_marks > 40:
        return "PASS"

    else:
        return "FAIL"


for i in range(5):
    print("\n\n========== STUDENT PERFORMANCE",i + 1 ,"==========")

    name = input("Enter Name :")
    math_marks = int(input("Enter Math Marks :"))
    science_marks = int(input("Enter Science Marks :"))
    py_marks = int(input("Enter Python Marks :"))
    jlpt_marks = int(input("Enter Japanese Marks :"))

    #Numpy array
    marks = np.array([
        math_marks,
        science_marks,
        py_marks,
        jlpt_marks
    ])

    all_marks.append([
        math_marks,
        science_marks,
        py_marks,
        jlpt_marks
    ])

    #Numpy calculation
    highest_marks = np.max(marks)
    lowest_marks = np.min(marks)

    total_marks =np.sum(marks)
    average_marks = np.mean(marks)

    student_grade = calculate_grade(total_marks)
    student_result = calculate_result(average_marks)


    student = {
        "name":name,
        "math":math_marks,
        "science":science_marks,
        "python":py_marks,
        "japanese":jlpt_marks,
        "total marks":total_marks,
        "Average":average_marks,
        "grade":student_grade,
        "result":student_result,
        "highest marks":highest_marks,
        "lowest marks":lowest_marks
    }

    students.append(student)

all_marks = np.array(all_marks)

print("\n========== NUMPY DATA ==========")
print(all_marks)
print("Shape :", all_marks.shape)

subject_average = np.mean(all_marks, axis=0)
subject_highest = np.max(all_marks, axis=0)
subject_lowest = np.min(all_marks, axis=0)
overall_average =np.mean(all_marks)
best_subject_index = np.argmax(subject_average)
student_total = np.sum(all_marks, axis=1)
highest_student_index = np.argmax(student_total)

print("\n========== OVERALL CLASS AVERAGE ===========")
print("OVERALL AVERAGE : ",overall_average)

print("\n========== HIGHEST SUBJECT STUDENT ==========")
print("MATH : ",subject_highest[0])
print("SCIENCE : ",subject_highest[1])
print("PYTHON : ",subject_highest[2])
print("JAPANESE : ",subject_highest[3])

print("\n========== LOWEST SUBJEST STUDENT ===========")
print("MATH : ",subject_lowest[0])
print("SCIENCE : ",subject_lowest[1])
print("PYTHON : ",subject_lowest[2])
print("JAPANESE : ",subject_lowest[3])

print("\n========== SUBJECT AVERAGE ==========")
print(subject_average)

highest_student =max(students, key=lambda x: x["total marks"]) 

# Dispkay Students

pass_count = 0
fail_count = 0

for student in students:
    print(
        student["name"],
        "|maTH :",student["math"],
        "|science :",student["science"],
        "|python :",student["python"],
        "|japanese :",student["japanese"],
        "|total marks :",student["total marks"],
        "|Average :",student["Average"],
        "|grade :",student["grade"],
        "|result :",student["result"]
    )
    if student["result"] == "PASS":
        pass_count += 1
    else:
        fail_count += 1

if best_subject_index == 0:
    best_subject = "Math"

elif best_subject_index == 1:
    best_subject = "Science"

elif best_subject_index == 2:
    best_subject = "Python"

elif best_subject_index == 3:
    best_subject = "Japanese"

print("\n========== BEST SUBJECT ==========")
print("Subject :", best_subject)
print("Average :", subject_average[best_subject_index])


print("\n========== CLASS RUSELT ==========")
print("PASS : ",pass_count)
print("FAIL : ",fail_count)

print("\n\n========== HIGEHEST STUDENT ==========")
print("NAME : ",highest_student["name"])
print("AVERAGE : ",highest_student["Average"],"%")
print("RESULT : ",highest_student["result"])
print("GRADE : ",highest_student["grade"])
print("HIGHEST MARKS : ",highest_student["highest marks"])
print("LOWEST MARKS : ",highest_student["lowest marks"])