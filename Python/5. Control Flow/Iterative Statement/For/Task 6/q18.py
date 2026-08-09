n = int(input("Enter the total number of participants: "))
for i in range(1,n+1):
    score = float(input("Enter the score of the participant: "))
    if score>400:
        print("Participant Number: P00"+str(i))