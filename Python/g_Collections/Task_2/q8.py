l1 = ["Aarav", "Diya", "Rohan"]
l2 = ["Priya", "Ananya", "Vikram","Diya"]
print(l1)
print(l2)
l1.extend(l2)
print("Combined list: ",l1)
for i in l1:
    if l1.count(i)>1:
        l1.remove(i)
print("Final List: ",l1)