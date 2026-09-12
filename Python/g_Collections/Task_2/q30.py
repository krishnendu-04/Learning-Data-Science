connected = {"dev_101", "dev_102", "dev_103", "dev_104", "dev_105"}
new_devices = {"dev_201", "dev_202", "dev_203", "dev_204", "dev_205"}
disconnected = ["dev_102", "dev_105"]
print("Connected devices: ",connected)
print("New devices: ",new_devices)
print("Discnonnected devices: ",disconnected)
connected.update(new_devices)
for i in disconnected:
    connected.remove(i)
print("Updated connected devices: ",connected)