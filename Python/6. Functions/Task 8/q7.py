def check_voting(age):
    if age>=18:
        print("You are eligible to vote")
    else:
        print("Not eligible to vote")

age = int(input("Enter your age: "))
check_voting(age)