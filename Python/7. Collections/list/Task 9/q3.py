contact_names = []
for i in range(5):
    contact_names.append(input("Enter the contact name: "))
print(contact_names)
print("Third contact: ",contact_names[2])
contact_names[1] = "Anu"
print("Updated list: ",contact_names)