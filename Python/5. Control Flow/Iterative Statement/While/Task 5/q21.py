password = input("Enter the password: ")
attempts = 1
if password=="helloworld":
        print("Logged in successfully")
while password!="helloworld" and attempts<3:
    password = input("Enter the password: ")
    attempts+=1
    if password=="helloworld":
        print("Logged in successfully")
        break
if attempts>=3:
    print("Phone Locked")