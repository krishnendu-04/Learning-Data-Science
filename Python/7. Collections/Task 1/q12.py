def branch_details():
    branches = ("Kochi", "Thiruvananthapuram", "Calicut (Kozhikode)", "Palakkad", "Kottayam", "Thrissur")
    print(branches)
    if "Kochi" in branches:
        print("Kochi branch exists")
    else:
        print("Kochi branch does not exist")
    print("Number of branches: ",len(branches))

branch_details()