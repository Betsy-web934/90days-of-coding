#RECURSION
#A function that calls itself until it reaches a base case. This is useful for problems that can be broken down into smaller subproblems.

#eg recursive function for an integer
def countdown(n):
    if n == 0:
        return
    print(n)

    countdown(n-2) # do one step at a time

countdown(6)

#Recursive function for a string
def hello(times):
    if times == 0: # the base case
        return
    print("Hello")
    hello(times-1)

hello(5)

def numbers(n):
    if n == 0:
        return
    print(n)
    numbers(n-1)

numbers(10)