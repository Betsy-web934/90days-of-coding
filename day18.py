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