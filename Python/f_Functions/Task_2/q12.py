def validate_password(password):
    if len(password)>=8:
        print("Password validated")
    else:
        print("Password not validated")

passw = input("Enter the password: ")
validate_password(passw)