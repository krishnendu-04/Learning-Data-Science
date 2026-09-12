r1 = open("dis_temp5.txt","r")
w1 = open("w5.txt","w")
dict1 = {}
for i in r1:
    rec = i.rstrip().split(",")
    if rec[0] not in dict1:
        dict1[rec[0]] = int(rec[1])
    else:
        if int(rec[1])>dict1[rec[0]]:
            dict1[rec[0]] = int(rec[1])
print(dict1)
for k,v in dict1.items():
    w1.write(f"{k}:{v}\n")