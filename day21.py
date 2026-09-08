#LIST COMPREHENSIONS -- 

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

#Traditional loop
numbers = [1, 2, 3, 4, 5]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
        print(even)

#List comprehensions
numbers = [1, 2, 3, 4, 5]
evens = [number for number in numbers if number % 2 == 0]
print(evens)