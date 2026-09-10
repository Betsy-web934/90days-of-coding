#searching and sorting in python

#searching
#it is finding a particular item in a collection

#sorting -- arranging items in a particular order

#SEARCHING
#Linear Search

students = ["John", "Alice", "Bob", "Eve", "Charlie"]

target = "Jane"
for student in students:
    if student == target:
        print("Found:", student)
        break
else:
    print("Not found")

#linear search with index
students = ["John", "Alice", "Bob", "Eve", "Charlie"]

target = "Bob"

for i in range(len(students)):
    if students[i] == target:
        print("Found:", students[i], "at index", i)
        break
else:
    print("Not found")

#Binary search
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

high = len(numbers) - 1
low = 0
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found:", numbers[mid], "at index", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

#sorting -- 
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)

print(sorted(numbers, reverse=True))  # Sort in descending order

#SORTED AND SORT
#sorted() -- returns a new list

numbers = [5, 2, 9, 1] # original list remains unchanged
new_numbers = sorted(numbers)
print(numbers)
print(new_numbers)

#sort() -- sort changes the original list
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # original list is modified

#how to sort strings
names = ["John", "Alice", "Bob", "Eve", "Charlie"]
sorted_names = sorted(names)
print("Sorted names:", sorted_names)

#bubble sort