signal = input("Enter the signal: ")
if signal=='Red' or signal=='red' or signal=='RED':
    print("Stop")
elif signal=='Yellow' or signal=='yellow' or signal=='YELLOW':
    print("Ready")
elif signal=='Green' or signal=='green' or signal=='GREEN':
    print("Go")
else:
    print("Invalid color for a traffic signal")