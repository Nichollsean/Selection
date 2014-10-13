#Sean Nicholls
#iteration hwk task 6.2

password = ""
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("You now have access to the system")
    else:
        print("Access Denied")
