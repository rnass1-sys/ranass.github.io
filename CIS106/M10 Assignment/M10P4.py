def compute_ticket_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5


total_ticket_sales = 0

while input("Do you want to enter data? (Yes/No): ").lower() == "yes":
    last_name = input("Enter last name: ")
    miles = float(input("Miles from downtown Chicago: "))

    ticket_price = compute_ticket_price(miles)
    total_ticket_sales += ticket_price

    print(f"Ticket Price for {last_name}: ${ticket_price:.2f}\n")

print(f"Total Ticket Sales: ${total_ticket_sales:.2f}")