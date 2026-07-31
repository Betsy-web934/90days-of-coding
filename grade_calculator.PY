#GRADE CALCULATOR
grade = float(input("Enter your grade: "))
print(f"Your grade is: {grade}")

if 80<=grade<=100:
    print(f"Your scored A")

elif 70<=grade<=79:
    print(f"Your scored B")

elif 60<=grade<=69:
    print(f"Your scored C")

elif 50<=grade<=59:
    print(f"You scored a D")

elif 40<=grade<=49:
    print(f"You scored an E")

else:
    print(f"You scored an F")