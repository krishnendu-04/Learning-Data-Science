def team_analysis():
    team_a = {
        "Alex Rivera",
        "Chris Jordan",
        "Jordan Lee",
        "Morgan Taylor",
        "Sam Smith",
        "Taylor Brooks",
    }
    team_b = {
        "Casey Miller",
        "Jamie Vance",
        "Jordan Lee",
        "Pat Kennedy",
        "Robin Diaz",
        "Skyler White",
    }
    print("Common players: ",team_a.intersection(team_b))
    print("Players only in Team A: ",team_a-team_b)
    print("All unique players: ",team_a.union(team_b))

team_analysis()