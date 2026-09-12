votes =["Aiswarya", "Vinu", "Reshma", "Akhil", "Reshma","Dhanya", "Reshma", "Akhil", "Dhanya"]
print(votes)
dict1 = {}
for i in votes:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1

high = 0
for value in dict1.values():
    if value>high:
        high = value

print("Candidate with highest vote: ")
for i in dict1:
    if dict1[i]==high:
        print(i)
        break
# cand = max(dict1,key=dict1.get)
# print("Candidate with highest votes: ",cand)