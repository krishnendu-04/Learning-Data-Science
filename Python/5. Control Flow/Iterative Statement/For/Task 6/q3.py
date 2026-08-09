for i in range(1,13):
    repair = input("Does the fan require repair? (y/n)")
    if repair=='y':
        print(i)
    elif repair=='n':
        pass
    else:
        print("Invalid answer")