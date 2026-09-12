runs_scored = [45, 102, 0, 76, 12, 54]
print(runs_scored)
centuries = 0
half_centuries = 0
for runs in runs_scored:
    if runs>=100:
        centuries+=1
    elif runs>=50:
        half_centuries+=1
print("Centuries: ",centuries)
print("Half Centuries: ",half_centuries)
runs_scored.sort()
print("Top 3 scores: ",runs_scored[-3:])