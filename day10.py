#ENCAPSULATION AND ACCESS MODIFIERS
#It's keeping the data safe and controlling how it is accessed
#ATM users insert a card input pin and withdraw money.

#ACCESS MODIFIERS
# 3 types Public members, Protected members and private members

#Public members are available everywhere
class Student:
    def __init__(self):
        self.name = "Betsy"

student = Student()
print(student.name)

#Protected Members
#They begin with underscore
class Bank:
    def __init__(self):
        self._balance = 900

bank = Bank()
print(bank._balance)

#PRIVATE MEMBERS
#They begin with two underscores
class Bank:
    def __init__(self):
        self.balance = 1000

bank = Bank()
print(bank.__balance)

#METHOD CONTROL DATA

#GETTERS AND SETTERS
#You might want to update private data safely
#Getters read value

def get__balance(self):
    return self.__balance

print(account.get__balance)

#Setters update the value after validation
def set__balance(self,amount):
    if amount >= 0:
        self.__balance = amount

    else:
        print(f"Invalid amount!!!")