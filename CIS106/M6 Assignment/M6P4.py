# M6P4: Concert Ticket Calculator

# 1. Get user input
tickets = int(input("Enter number of concert tickets: "))

# 2. Determine price per ticket using volume else-if checks
if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10 and tickets <= 24:
    price_per_ticket = 60.00
elif tickets >= 5 and tickets <= 9:
    price_per_ticket = 70.00
else:  # Less than 5
    price_per_ticket = 75.00

# 3. Calculate total cost
total_cost = tickets * price_per_ticket

# 4. Display results with decimals aligned in columns
print("\n--- Ticket Receipt ---")
print(f"{"Number of Tickets:":<20} {tickets:>13}")
print(f"{"Price per Ticket:":<20} ${price_per_ticket:>12,.2f}")
print(f"{"Total Cost:":<20} ${total_cost:>12,.2f}")
