employee = [[101,"vinay",30,"data scientist",50000],[102,"aryan",27,"sales person",20000],[103,"anu",24,"engineer",45000],[104,"siya",28,"HR",80000],[105,"diya",23,"IT Manager",35000]]
for i in employee:
    if i[2]>=30:
        print(i[1])

    if i[3]=="data scientist":
        print(i[1:3])