n = int(input("Enter the amount: "))
rs500 = n//500
remain = n%500
rs200 = remain//200
remain1 = remain%200
rs100 = remain1//100
remain2 = remain1%100
rs50 = remain2//50
remain3 = remain2%50
rs20 = remain3//20
remain4 = remain3%20
rs10 = remain4//10
remain5 = remain4%10
rs5 = remain5//5
remain6 = remain5%5
rs2 = remain6//2
remain7 = remain6%2
print("Denominations are as follows: ")
print("500: ",rs500,"\n200: ",rs200,"\n100: ",rs100,"\n50: ",rs50,"\n20: ",rs20,"\n10: ",rs10,"\n5: ",rs5,"\n2: ",rs2,"\n1: ",remain7)