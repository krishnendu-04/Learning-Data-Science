def training_report():
    python = {
        "Aarav",
        "Amit",
        "Diya",
        "Kabir",
        "Riya",
        "Vivaan",
    }

    sql = {
        "Amit",
        "Arjun",
        "Diya",
        "Isha",
        "Karan",
        "Neha",
    }
    print("Employees who completed both training:\n ",python.intersection(sql))
    print("Employees who completed only python:\n ",python-sql)
    print("All trained employees:\n ",python.union(sql))

training_report()