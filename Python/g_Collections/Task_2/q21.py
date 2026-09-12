stations = (
    "Thiruvananthapuram Central",
    "Ernakulam Junction",
    "Kozhikode Main",
    "Thrissur",
    "Kollam Junction",
    "Palakkad Junction",
    "Alappuzha",
    "Kottayam",
    "Kannur",
    "Shoranur Junction"
)
print(stations)
print("\nStations between 3rd and 7th stations: ")
for i in range(len(stations)):
    if 3<i<7:
        print(stations[i])