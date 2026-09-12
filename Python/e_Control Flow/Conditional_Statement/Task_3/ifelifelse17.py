use = float(input("Enter the data usage in GBs: "))
if use<1:
    print("Rs.150")
elif 1<=use<2.5:
    print("Rs.399")
elif 2.5<=use<5:
    print("Rs.599")
elif use>=5:
    print("999")
else:
    print("Plan not available")