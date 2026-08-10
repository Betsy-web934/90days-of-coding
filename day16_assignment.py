#STUDENT DICTIONARY
dictionary = {
    "name": "John",
    "age": 21,
    "university": "Zetech University",
    "course": "Software Engineering",
    "favourite_programming_language": "Python"
}

print(dictionary["name"])
print(dictionary.get("university"))

#add a new key called email
dictionary["email"] = "jk@gmail.com"
print(dictionary["email"])

#update the value of the key age to 22
dictionary["age"] = 22

#remove the key called favourite_programming_language
del dictionary["favourite_programming_language"]

print(dictionary)

#LIBRARY MANAGEMENT SYSTEM
dictionary2 = {
    "title" : "Psychlogy of Money",
    "author" : "Morgan Housel",
    "year" : 2020,  
    "price" : 25.99,
    "available" : True
}

dictionary2["price"] = 20.99
dictionary2["genre"] = "Finance"

#dispaly all the keys in the dictionary
print(dictionary2.keys())

#Display all the values in the dictionary
print(dictionary2.values())


print(dictionary2)

#Display every key together with its value using a for loop
for key, value in dictionary2.items():
    print(key, ":", value)

#NESTED DICTIONARIES
dictionary3 = {
    "student1": {
        "name": "Alice",
        "admission_number": "A001",
        "course": "Computer Science",
        "year": 2022
    },
    "student2": {
        "name": "Bob",
        "admission_number": "A002",
        "course": "Information Technology",
        "year": 2021
    },
    "student3": {
        "name": "Charlie",
        "admission_number": "A003",
        "course": "Software Engineering",
        "year": 2020
    }
}

#print name of student2
print(dictionary3["student2"]["name"])
print(dictionary3["student3"]["course"])

#loop through the nested dictionary and display each student's details
for key, value in dictionary3.items():
    print(key, ":", value)

#JSON CONVERSION
import json

student = {
    "name": "John",
    "age": 21,
    "university": "Zetech University",
    "course": "Software Engineering",
    "favourite_programming_language": "Python"
}

#convert the dictionary into JSON uisng json.dumps()
student_json = json.dumps(student)
print(student_json) #print the json data

#convert json back to a pthon dictionary using json.loads()
student_dict = json.loads(student_json)
print(student_dict)

print(student_dict["course"])

# QUESTION 5 :SCOPE
#create a global variable called school
school = "Makini Academy"

def print_school():
    print(school)

print_school()
#create a local variable called student

def person():
    student = "Betsy"
    print(student)

#print(student) ---- this will turn out to be an error coz student only exists in the function person

#attempt to print the local variable outside the function and observe the error
#student()

#RECURSIVE COUNTDOWN
def countdown(n):
    if n < 0:
        return
    print(n)

    countdown(n - 1)
n = int(input("Enter a number: "))
countdown(n)
