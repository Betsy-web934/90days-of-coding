#Big-O gives a way of describing how the amount of work grows as the input gets larger.

#O(1) - Constant Time complexity

students = ["Alice", "Bob", "Charlie", "David"]
print(students[0])

#O(n) - Linear Time
#work grows linearly with the input size

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

#O(n^2) - Quadratic Time
#work grows quadratically with the input size

numbers = [1, 2, 3, 4, 5]
for x in numbers:
    for y in numbers:
        print(x, y) 

#O(log n) - Logarithmic Time

