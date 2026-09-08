#A python program that analyzes student information using lists,dictionaries, sets and comprehensions.

print("===================== Student Data Analyzer ====================")


students = [
    {
        "name": "John",
        "course": "Computer Science",
        "marks": 78
    },

    {
        "name": "Mary",
        "course": "Information Technology",
        "marks": 91
    },

    {
        "name": "Brian",
        "course": "Computer Science",
        "marks": 64
    },

    {
        "name": "Jane",
        "course": "Data Science",
        "marks": 85
    },

    {
        "name": "David",
        "course": "Information Technology",
        "marks": 48
    }
]

#create a list containing only names of students
student_names = [student["name"] for student in students]
print("Student Names:", student_names)

#create a list of the name of students who scored above 50 marks and above
passing_students = [student["name"] for student in students if student["marks"] > 50]
print("Passing Students:", passing_students)

#Create a list of students who scored above 80 marks and above
top_students = [student["name"] for student in students if student["marks"] > 80]
print("Top Students:", top_students)

#Create a set of all unique courses
courses = {student["course"] for student in students}
print("Unique Courses:", courses)

#Create a dictionary that outputs student names and their corresponding marks (Dictionary Comprehension)
student_marks = {student["name"]: student["marks"] for student in students}
print("Student Marks:", student_marks)

#Create a dictionary where there is a student name and their grades( from A - F)
for student in students:
    if student["marks"] >= 80:
        student["grade"] = "A"
    elif student["marks"] >= 70 and student["marks"] < 80:
        student["grade"] = "B"
    elif student["marks"] >= 60 and student["marks"] < 70:
        student["grade"] = "C"
    elif student["marks"] >= 50 and student["marks"] < 60:
        student["grade"] = "D"
    else:
        student["grade"] = "F"
student_grades = {student["name"]: student["grade"] for student in students}
print("Student Grades:", student_grades)

#Calculate and display average marks of all students
total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / len(students)
print("Average Marks:", average_marks)

#ask a user to input a course name and display the names of students enrolled in that course
course_name = input("Enter a course name to find students enrolled in that course: ")
enrolled_students = [student["name"] for student in students if student["course"] == course_name]
print(f"Students enrolled in {course_name}: {enrolled_students}")

print("===================== End of Student Data Analyzer ====================")