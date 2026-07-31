balance = 10000

choose = input("Enter your choice: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit: ")

if choose == "1":
    print(f"Your balance is {balance}")
elif choose == "2":
    deposit = int(input("How much do you want to deposit: "))
    if deposit <= 0:
        print(f"Input a valid amount")
    else:
        balance = balance + deposit
        print(f"Your new balance is {balance}")

elif choose == "3":
    withdraw = int(input("How much do you want to withdraw:"))
    if withdraw > balance:
        print("Insufficient funds!")

    else:
        new_balance = balance - withdraw
        print(f"Your new balance is: {new_balance}")

elif choose == "4":
    print("Thank you for using our services!")
else:
    print("Invalid choice. Please try again.")