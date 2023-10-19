correct_password = "DEV@2023"
attempts = 3

for i in range(attempts):
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Hello")
        break
else:
    answer = input("You have exhausted your attempts. What is your favorite movie? ")
    if answer == "The Matrix":
        print("Hello")
    else:
        print("Access denied.")
