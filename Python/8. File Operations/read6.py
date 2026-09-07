file = open("r6.txt","r")
for i in file:
    lst1 = i.rstrip("\n").split(',')
    if int(lst1[2])==21:
        print(i)

    if int(lst1[2])>22:
        print(lst1[:-1])

    if int(lst1[2])<23:
        print(lst1[0:2],lst1[-1])

    if lst1[-1]=="Ernakulam":
        print(lst1[:-1])

    if lst1[-1]=="Thrissur" and int(lst1[2])>23:
        print(lst1[::2])