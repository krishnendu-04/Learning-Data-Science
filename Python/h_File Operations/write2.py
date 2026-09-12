r1 = open("w2_fruits.txt","r")
w1 = open("w2_fruits_copy.txt","w")
for i in r1:
    w1.write(i)