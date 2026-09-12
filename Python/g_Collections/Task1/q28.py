def club_members():
    science = {
        "Aarav",
        "Amit",
        "Diya",
        "Kabir",
        "Riya",
        "Vivaan",
    }
    arts = {
        "Amit",
        "Arjun",
        "Diya",
        "Isha",
        "Karan",
        "Neha",
    }
    print("Students in both club:\n ",science.intersection(arts))
    print("Students in only one club: \n",science.union(arts)-science.intersection(arts))
    print("All members:\n ",science.union(arts))


club_members()