n = int(input("Enter the number of laptops: "))
for i in range(n):
    serial = input("Enter the serial number of the laptop: ")
    status = input("Did it Pass/Fail the inspection: ")
    if status=="Fail" or status=="fail" or status=="FAIL":
        print(serial)