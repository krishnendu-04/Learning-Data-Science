def weather_analysis():
    weekly_temps = (72, 75, 68, 71, 74, 79, 73)
    print(weekly_temps)
    avg = 0
    for i in weekly_temps:
        avg+=i
    avg/=len(weekly_temps)
    print("Average temperature: ",avg)
    print("Maximum temperature: ",max(weekly_temps))
    print("Minimum temperature: ",min(weekly_temps))

weather_analysis()