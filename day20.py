#SETS -- is a collection of unique elements

fruits = {"Banana", "Mango"}
print(fruits)

#List we use square brackets whereas Sets use curly brackets
#Set does not allow duplicate values
#SET supprots mathematical set operators

#CREATING SETS
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)

numbers = set([9, 8, 7, 0])
print(numbers)

#Connvert a list to a set
names = ["Job", "Joel", "Mark", "lucy"]

first_names = set(names)
print(first_names)

#creating an empty set
my_set = set()
print(type(my_set))

#MISTAKES TO AVOID
my_set = {} # this is a dictionary not set
print(type(my_set))

#sets remove duplicates
numbers = {1, 1, 2, 2, 3, 3, 9, 9, 9}
print(numbers)

name = {
    "Betsy",
    "Kimani",
    "Joleen",
    "Kimani"
}
print(name)

#sets are unordered
number = {10, 20, 30, 40, 50}
print(number)

#Adding elements
student = {"Joshua", "Kering","Stacy"}
student.add("Peter")
print(student)

#ADD multiple elemts
student.update(["David", "Alice"])
print(student)

#removing elements : 3 methods
student.remove("Stacy")
print(student)

student.discard("Jane")
print(student)

student = student.pop()
print(student) 

#MEMBERSHIP TESTING 
animals = {"Man", "Lion", "Giraffe"}
print("Elephant" in animals)
#LOOPING THROUGH THE SETS
for animal in animals:
    print(animal)

#COMPARING SETS
python_students = {"Mary", "Jason", "Charlie", "Ben"}
java_students = {"Mary", "Jason", "Ted", "Prian"}

all_students = python_students.union(java_students)
print(all_students)

#INTERSECTION - gives elements belonging to the same set
common_students = python_students.intersection(java_students)
print(common_students)

only_python = python_students.difference(java_students)
print(only_python)

#SYMMETRIC DIFFERENCE -- elemts that exist in either set but not both of them
result = python_students.symmetric_difference(java_students) 
print(result)

#SET OPERATIONS
#SUB-SETS AND SUPER SETS REMOVING DUPLICATES FROM A LIST