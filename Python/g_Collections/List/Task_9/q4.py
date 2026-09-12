runs = []
for i in range(6):
    runs.append(int(input("Enter the runs scored in each over: ")))
print(runs)
print("Total runs: ",sum(runs))
print("Highest score: ",max(runs))