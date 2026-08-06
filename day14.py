#FUNCTION ARGUMENTS AND SCOPE
#We learn how to make our function much smarter

def order_pizza(size, toppings):
    print(f"{size} pizza with {toppings} toppings")
order_pizza("large", "pepperoni")

#1. POSITIONAL ARGUMENTS
#The depend on the order

def student(name,age):
    print(name, age)

student("Betsy", 18)

#2. KEYWORD ARGUMENTS
#Let's us specifyn which value belongs to which parameter

student(age=21, name="Job")
#default arguments 

#3. DEFAULT ARGUMENTS

def pay(amount, currency="Kshs"):
    print(f"You have paid {amount} {currency}")
pay(500)

#custom currency
pay(500, "USD")


#SCOPE
#Scope --Region where a variable is accessible

##1. Local Scope
#exists only inside the function

def test():
    x = 10
    print(x)

test()

#2. Global Scope
#Created outside the function and can be accessed anywhere in the program
