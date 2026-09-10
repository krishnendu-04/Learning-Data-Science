def football_team(players):
    injured = input("Enter the name of the injured player: ")
    if injured in players:
        ind = players.index(injured)
        players.remove(injured)
        print("After removal of injured player: ",players)
        players.insert(ind,input("Enter the name of the player to replace with: "))
        print("Updated players: ",players)
    else:
        print("Invalid player")
    players.sort()
    for i in players:
        print(i)


n = int(input("Enter the number of players: "))
players = []
for i in range(n):
    players.append(input("Enter the name of the players: "))
football_team(players)