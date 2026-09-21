#coding Friday

cars = ['bmw', 'audi', 'toyota', 'subaru']
target = "Toyota"

for car in cars:
    if car == target.lower():
        print(car.title())

def linear_search(items, target):

    for item in items:
        if item == target:
            return True
    return False

students = ['Alice', 'Bob', 'Charlie', 'David']
result = linear_search(students, 'Charlie')

print(result)  # Output: True

#sorting
numbers = [1000, 950, 600, 400, 200, 100]
numbers.sort()
print(numbers)  # Output: [100, 200, 400, 600, 950, 1000]

#BUBBLE SORT --

numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted array is:", numbers)