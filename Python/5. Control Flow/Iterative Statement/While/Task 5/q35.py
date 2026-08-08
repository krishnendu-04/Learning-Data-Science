total = 0
votes = input("Enter the votes for candidates: ")
while votes!='stop':
    total+=(int(votes))
    votes = input("Enter the votes for candidates: ")
print("Total votes: ",total)