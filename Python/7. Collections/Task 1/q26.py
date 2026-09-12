def blood_bank():
    blood_grps = {
        "A+",
        "A-",
        "AB+",
        "AB-",
        "B+",
        "B-",
        "O+",
        "O-",
    }
    print(blood_grps)
    requested = input("Enter the required blood group: ")
    if requested in blood_grps:
        print("Requested blood group available")
    else:
        print("Requested blood group not available")
    donated = input("Enter the newly donated blood group: ")
    blood_grps.add(donated)
    print("Available blood groups: ")
    for i in blood_grps:
            print(i)

blood_bank()