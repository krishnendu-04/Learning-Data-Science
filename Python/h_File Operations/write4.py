r1 = open("customer4.txt","r")
w1 = open("w4_prof_count.txt","w")
dict1 = {}
for i in r1:
    rec = i.rstrip("\n").split(",")
    if rec[4] not in dict1:
        dict1[rec[4]] = 1
    else:
        dict1[rec[4]]+=1
for key,value in dict1.items():
    w1.write(f"{key}:{value}\n")