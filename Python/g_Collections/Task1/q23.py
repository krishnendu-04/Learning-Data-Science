def event_registration():
    reg_studs = {
        "STU1042",
        "STU2915",
        "STU3840",
        "STU4721",
        "STU5106",
        "STU6394",
        "STU7712",
        "STU8249",
        "STU9053",
        "STU9861",
    }
    print(reg_studs)
    reg_studs.add("STU4353")
    print("\nUpdated set after adding new student : ",reg_studs)
    print()
    for i in reg_studs:
        print(i)

event_registration()