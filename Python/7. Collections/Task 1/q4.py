def cricket_stats(runs):
    total = 0
    highest = runs[0]
    half_cen = 0
    for i in runs:
        total+=i
        if i>highest:
            highest = i
        if 50<=i<=99:
            half_cen+=1
    print("Total runs: ",total)
    print("Highest score: ",highest)
    print("Number of half centuries: ",half_cen)

n = int(input("Enter the number of matches: "))
runs = []
for i in range(n):
    runs.append(int(input("Enter the runs scored: ")))
cricket_stats(runs)