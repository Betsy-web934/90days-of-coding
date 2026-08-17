# LISTS AND TUPLES
#LIST - We are storing multiple values in a single variable.

student1 = "Mary"
student2 = "John"
student3 = "Alice"
student4 = "Bob"

students = ["Mary", "John", "Alice", "Bob"]  # This is a list
numbers = [1, 2, 3, 4, 5, 6.7, 5.9]  # This is also a list of numbers
mixed = ["John", 29, True, 5.6]  # This is a mixed list


#List indexing
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

print(fruits[0])
#negative indexing
print(fruits[-1])

#Changing list elments
fruits[0] = "orange"

print(fruits)

#Adding elements to a list
#append() - adds an element to the end of the list
workers = ["John", "Alice", "Bob"]
workers.append("Mary")
print(workers)

#insert() - adds an element at a specific index
workers.insert(1, "JOB")
print(workers)

#extend() - adds multiple elements to the end of the list
workers.extend(["Ruth", "Joel"])
print(workers)

#Removing elements 
#remove -- removes a specific value
cars = ["Honda", "Benz", "Toyota", "BMW"]
cars.remove("Honda")
print(cars)

#pop -- removes the element using its index
cities = ["Nairobi", "Mombasa", "Eldoret", "Kisumu"]
cities.pop(1)
print(cities)

#delete
towns = ["Machackos", "Eastleigh", "Mirema"]
del towns[1]
print(towns)

#clear -- removes everything from the list
presidents = ["Jomo", "Moi", "Kibaki", "Ruto"]
presidents.clear()
print(presidents)

#List slicing
numberz = [10, 20, 30, 40, 50, 60]
print(numberz[1:4])
print(numberz[:3])
print(numberz[2:])

#Finding the length of a list
#len()
days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
print(len(days))


#Checking if an element exists
print("Friday" in days)
print("Monday" in days)

#Looping through elements

for day in days:
    print(days)

#Nested lists
studentz = [
    ["John", 20],
    ["Mary", 30]
]

print(studentz[0])

#TUPLES - are immutable
coordinates = (10,20)
print(coordinates[0])