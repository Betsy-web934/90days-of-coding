# MODULES, PACKAGES AND FILE HANDLING

#MODULES - Python file that contains code that can be used in any program
# eg apps like facebook, whatsapp, instagram, etc are all modules

#import math as m
# print(m.factorial(6))

#PACKAGES - A folder containing multiple related modules

#FILE HANDING - Python provides built-in functions to create, read, update and delete files
#Opening a file in read mode
# file = open(filename, mode)
file = open("student_record.py", "r")
print(file.read())
file.close()

# reading file line by line
file = open("student_record.py", "r")
for line in file:
    print(line)

file.close()

# writing a file
file = open("grade_calculator.py", "w")

file.write("simple calculator to calculate grades\n")
file.close() 

# Appendding to a file
file = open("grade_calculator.py", "a")
file.write("additional information\n")
file.close()

# using with - not a must to close the file after opening it
with open("grade_calculator.py", "r") as file:
    print(file.read())