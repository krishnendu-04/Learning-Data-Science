def scoreboard():
    cricket_scores = {
        "Virat": 85,
        "Rohit": 42,
        "Dhoni": 104,
        "Kohli": 67,
        "Jadeja": 25
    }
    print(cricket_scores)
    max_runs = 0
    for i in cricket_scores:
        if cricket_scores[i]>max_runs:
            max_runs = cricket_scores[i]
            max_scored = i
    print("Maximum runs scored by: ",max_scored)
    for j in cricket_scores:
        if cricket_scores[j]>50:
            print(j,"scored more than 50 runs")

scoreboard()