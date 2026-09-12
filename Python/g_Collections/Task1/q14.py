def medal_count():
    medals = (40, 44, 42)
    total = 0
    for i in medals:
        total+=i
    print("Total medal count: ",total)
    print("Highest medal count: ",max(medals))

medal_count()