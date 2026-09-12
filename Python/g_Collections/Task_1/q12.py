def branch_details():
    branches = ("Kochi", "Thiruvananthapuram", "Kozhikode", "Palakkad", "Kottayam", "Thrissur")
    print(branches)
    if "Kochi" in branches:
        print("Kochi branch exists")
    else:
        print("Kochi branch does not exist")
    print("Number of branches: ",len(branches))

branch_details()