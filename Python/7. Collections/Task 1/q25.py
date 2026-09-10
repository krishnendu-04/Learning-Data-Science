def skill_analysis():
    emp_a = {
        "Data Analysis",
        "Java",
        "Project Management",
        "Python",
        "SQL",
    }
    emp_b = {
        "Cloud Computing",
        "DevOps",
        "JavaScript",
        "Python",
        "SQL",
    }
    print("Common skills: ",emp_a.intersection(emp_b))
    print("Unique skills: ",emp_a.union(emp_b))
    emp_a.update(emp_b)
    for i in emp_a:
        print(i)

skill_analysis()