# Simple course registration using lists, tuples and sets

#set of python_students
python_students = {
    "John",
    "Mary",
    "David",
    "Alice"
}
print(python_students)

web_students = {
    "Mary",
    "Alice",
    "Peter",
    "James"
}
print(web_students)

#Find students taking both courses, SETS removes duplicates, comparing setszz


student_details = [
    ("John", 20, "Computer Science"), #tuples
    ("Mary", 21, "Computer Science"),
    ("David", 19, "Information Technology"),
    ("Alice", 20, "Computer Science"),
    ("Peter", 22, "Software Engineering"),
    ("James", 21, "Computer Science")
]

#find students taking both courses

repeated_elements = python_students & web_students

print("This are students taking both python and web:",repeated_elements)

#find students taking only python
only_python = python_students.difference(web_students)
print("These are the only students taking python: ",only_python)

#find students taking only web development
only_web = web_students.difference(python_students)
print("These are students taking web development only: ",only_web)

#display unique students
unique_students = python_students.symmetric_difference(web_students)
print("Unique students:",unique_students)

#number of unique students
print("Total unique students:",len(unique_students))

#loop through student details and display name and course
for students in student_details:
    print(students)

#search for a student by name
name = input("Enter name of student you want to search: ")
found = False
for person in student_details:
    if person[0] == name:
        print("Student exists",person) 
        if name in python_students & web_students:
            print("This student is registered for both python and web")

        elif name in only_python:
            print("This student is registered for only python")

        elif name in web_students:
            print("This student is registered for web")
        found = True
        break

if not found:
    print("Student not found")

