def water_bill(units_kl):
    if 0<units_kl<=10:
        rate = units_kl*5
        print("Slab wise rate: ",rate)
    elif 11<=units_kl<=20:
        rate = units_kl*10
        print("Slab wise rate: ",rate)
    elif 21<=units_kl<=30:
        rate = units_kl*20
        print("Slab wise rate: ",rate)
    elif units_kl>30:
        rate = units_kl*40
        print("Slab wise rate: ",rate)
    print("Fixed meter rent: ",50)
    print("Total amount: ",rate+50)


units = int(input("Enter the water consumed in kl: "))
water_bill(units)