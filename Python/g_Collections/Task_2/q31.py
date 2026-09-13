blood_donor = {
    "DONOR-8819",
    "DONOR-4402",
    "DONOR-1193",
    "DONOR-5571",
    "DONOR-3048",
    "DONOR-9210",
    "DONOR-7745",
}
print(blood_donor)
reg = input("Enter the donor ID received to register: ")
if reg in blood_donor:
    print("Donor already regsitered!")
else:
    blood_donor.add(reg)
    print(blood_donor)