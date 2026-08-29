def ticket_price(no_of_tickets):
    return no_of_tickets*150
n = int(input("Enter the number of tickets: "))
rate = ticket_price(n)
print("Total amount: ",rate)