#LOG IN SYSTEM
username = "THURSDAY"
password = "90DAYS" 

while True:
    user_input = input("Enter your username: ")
    password_input = input("Enter your password:")

    if user_input == username and password_input == password:
        print("Access granted. Welcome!")
        break

    else:
        print("Access denied. Please try again.")
        break